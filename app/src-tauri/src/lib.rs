//! Tauri 後端：把判題核心（cpe-judge）與考試狀態（session）包成前端可以呼叫的 command。
//!
//! 編譯與執行都是阻塞操作，一律丟到 blocking 執行緒，避免卡住 UI。
//! 考試狀態有變動時廣播 `session-changed`，讓所有視窗同步。

mod session;
mod statements;

use cpe_judge::{
    builtin_languages, list_problems, load_problem, load_tests, toolchain, Compiled, JudgeEnv, Language,
    ProblemMeta, ProcStatus, TestCase, TestSet, Verdict,
};
use serde::{Deserialize, Serialize};
use session::{now_ms, CodeDraft, Examinee, PlannedExam, SavedCode, Session, Store};
use statements::StatementCache;
use std::collections::HashMap;
use std::path::PathBuf;
use std::sync::{Arc, Mutex};
use std::time::Duration;
use tauri::{AppHandle, Emitter, Manager, State, WebviewUrl, WebviewWindowBuilder};

struct AppState {
    problems_dir: PathBuf,
    env: JudgeEnv,
    store: Store,
    statements: StatementCache,
    session: Mutex<Session>,
    /// 編譯好的標準解，用來產生自訂測資的「正確輸出串」。
    reference: Mutex<HashMap<String, Arc<Compiled>>>,
}

type CmdResult<T> = Result<T, String>;

fn err(e: impl std::fmt::Display) -> String {
    e.to_string()
}

fn language(id: &str) -> CmdResult<Language> {
    builtin_languages().into_iter().find(|l| l.id == id).ok_or_else(|| format!("未知的語言：{id}"))
}

async fn blocking<T: Send + 'static>(f: impl FnOnce() -> CmdResult<T> + Send + 'static) -> CmdResult<T> {
    tauri::async_runtime::spawn_blocking(f).await.map_err(err)?
}

fn problem_dir(state: &AppState, id: &str) -> CmdResult<PathBuf> {
    if id.is_empty() || !id.chars().all(|c| c.is_ascii_alphanumeric()) {
        return Err(format!("題號格式錯誤：{id}"));
    }
    Ok(state.problems_dir.join(format!("uva-{id}")))
}

/// 修改 Session、存檔並通知所有視窗。
fn update_session<T>(app: &AppHandle, f: impl FnOnce(&mut Session) -> T) -> CmdResult<T> {
    let state = app.state::<AppState>();
    let mut s = state.session.lock().map_err(err)?;
    let out = f(&mut s);
    state.store.save_session(&s).map_err(err)?;
    app.emit("session-changed", &*s).map_err(err)?;
    Ok(out)
}

// ───────────── 環境 ─────────────

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
struct ToolchainReport {
    command_line_tools_installed: bool,
    tools: Vec<toolchain::ToolStatus>,
}

#[tauri::command]
async fn toolchain_status(state: State<'_, AppState>) -> CmdResult<ToolchainReport> {
    let extra = state.env.extra_paths.clone();
    blocking(move || {
        Ok(ToolchainReport {
            command_line_tools_installed: toolchain::command_line_tools_installed(),
            tools: toolchain::detect(&builtin_languages(), &extra),
        })
    })
    .await
}

#[tauri::command]
fn install_command_line_tools() -> CmdResult<()> {
    toolchain::request_command_line_tools_install().map_err(err)
}

#[tauri::command]
fn languages() -> Vec<Language> {
    builtin_languages()
}

// ───────────── 題目 ─────────────

#[tauri::command]
fn problems(state: State<'_, AppState>) -> CmdResult<Vec<ProblemMeta>> {
    Ok(list_problems(&state.problems_dir).map_err(err)?.into_iter().map(|p| p.meta).collect())
}

#[derive(Serialize)]
struct ProblemDetail {
    meta: ProblemMeta,
    statement: String,
}

#[tauri::command]
fn problem(state: State<'_, AppState>, id: String) -> CmdResult<ProblemDetail> {
    let p = load_problem(&problem_dir(&state, &id)?).map_err(err)?;
    Ok(ProblemDetail { meta: p.meta, statement: p.statement })
}

/// 題目原文 PDF（和考場一樣直接顯示）。回傳原始 bytes，前端用 pdf.js 繪製。
#[tauri::command]
async fn problem_pdf(app: AppHandle, id: String) -> CmdResult<tauri::ipc::Response> {
    blocking(move || {
        let state = app.state::<AppState>();
        let p = load_problem(&problem_dir(&state, &id)?).map_err(err)?;
        let uva = p.meta.uva.ok_or("這一題沒有 UVa 編號")?;
        let bytes = state.statements.get(uva, &statements::default_sources(uva))?;
        Ok(tauri::ipc::Response::new(bytes))
    })
    .await
}

// ───────────── 測試與評判 ─────────────

/// 單筆測試的完整資料，給「建置測試」面板顯示。
#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
struct TestCaseView {
    name: String,
    verdict: Verdict,
    input: String,
    /// 正確輸出串；標準解無法執行時為 None。
    expected: Option<String>,
    stdout: String,
    stderr: String,
    time_ms: u64,
    expected_time_ms: Option<u64>,
}

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
struct TestRun {
    verdict: Verdict,
    compile_message: Option<String>,
    cases: Vec<TestCaseView>,
}

fn lossy(b: &[u8]) -> String {
    String::from_utf8_lossy(b).into_owned()
}

fn compile_or_report(lang: &Language, source: &str, env: &JudgeEnv) -> Result<Compiled, TestRun> {
    cpe_judge::compile(lang, source, env).map_err(|e| TestRun {
        verdict: Verdict::CompilerError,
        compile_message: Some(e.message),
        cases: vec![],
    })
}

/// 題目預設測試資料（sample）或人工公開測試資料（public），不列入成績。
#[tauri::command]
async fn run_tests(state: State<'_, AppState>, id: String, lang: String, source: String, set: TestSet) -> CmdResult<TestRun> {
    if set == TestSet::Hidden {
        return Err("暗中測試資料只能用於正式評判".into());
    }
    let dir = problem_dir(&state, &id)?;
    let env = state.env.clone();
    blocking(move || {
        let p = load_problem(&dir).map_err(err)?;
        let cases = load_tests(&p, set).map_err(err)?;
        let compiled = match compile_or_report(&language(&lang)?, &source, &env) {
            Ok(c) => c,
            Err(report) => return Ok(report),
        };
        let views: Vec<TestCaseView> = cases
            .iter()
            .map(|case| {
                let r = compiled.run_case(case, p.time_limit());
                TestCaseView {
                    name: r.name,
                    verdict: r.verdict,
                    input: lossy(&case.input),
                    expected: Some(lossy(&case.output)),
                    stdout: r.stdout,
                    stderr: r.stderr,
                    time_ms: r.time_ms,
                    expected_time_ms: None,
                }
            })
            .collect();
        let verdict = views.iter().map(|v| v.verdict).find(|v| *v != Verdict::Correct).unwrap_or(Verdict::Correct);
        Ok(TestRun { verdict, compile_message: None, cases: views })
    })
    .await
}

/// 取得（必要時編譯）某題的標準解。
fn reference_solution(state: &AppState, id: &str, dir: &std::path::Path) -> CmdResult<Arc<Compiled>> {
    if let Some(c) = state.reference.lock().map_err(err)?.get(id) {
        return Ok(c.clone());
    }
    let source = std::fs::read_to_string(dir.join("sol.cpp")).map_err(|e| format!("找不到標準解：{e}"))?;
    let compiled = cpe_judge::compile(&language("ccpp")?, &source, &state.env)
        .map_err(|e| format!("標準解編譯失敗：{}", e.message))?;
    let compiled = Arc::new(compiled);
    state.reference.lock().map_err(err)?.insert(id.to_string(), compiled.clone());
    Ok(compiled)
}

/// 使用自訂測試資料：同時執行考生程式與標準解，並比對輸出（不列入成績）。
#[tauri::command]
async fn run_custom(app: AppHandle, id: String, lang: String, source: String, input: String) -> CmdResult<TestRun> {
    blocking(move || {
        let state = app.state::<AppState>();
        let dir = problem_dir(&state, &id)?;
        let p = load_problem(&dir).map_err(err)?;
        let compiled = match compile_or_report(&language(&lang)?, &source, &state.env) {
            Ok(c) => c,
            Err(report) => return Ok(report),
        };
        let out = compiled.run(input.as_bytes(), p.time_limit()).map_err(err)?;
        let reference = reference_solution(&state, &id, &dir)
            .ok()
            .and_then(|r| r.run(input.as_bytes(), p.time_limit()).ok())
            .filter(|r| r.status == ProcStatus::Exited(0));
        let verdict = match &reference {
            Some(r) => cpe_judge::verdict_for(&out, &r.stdout, p.time_limit()),
            // 沒有標準輸出可比對時，只看程式本身有沒有正常結束。
            None => cpe_judge::verdict_for(&out, &out.stdout, p.time_limit()),
        };
        Ok(TestRun {
            verdict,
            compile_message: None,
            cases: vec![TestCaseView {
                name: "custom".into(),
                verdict,
                input,
                expected: reference.as_ref().map(|r| lossy(&r.stdout)),
                stdout: lossy(&out.stdout),
                stderr: lossy(&out.stderr),
                time_ms: out.elapsed.as_millis() as u64,
                expected_time_ms: reference.as_ref().map(|r| r.elapsed.as_millis() as u64),
            }],
        })
    })
    .await
}

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
struct FormalResult {
    verdict: Verdict,
    compile_message: Option<String>,
    /// 這一題至今的正式評判次數（含這一次）。
    attempts: usize,
}

#[derive(Deserialize, Clone, Copy, PartialEq, Eq)]
#[serde(rename_all = "lowercase")]
enum Mode {
    Exam,
    Practice,
}

/// 正式評判：用暗中測試資料，遇到第一筆錯誤就停。考試模式會記錄送繳（列入成績）。
#[tauri::command]
async fn formal_judge(app: AppHandle, mode: Mode, id: String, lang: String, source: String) -> CmdResult<FormalResult> {
    // 先檢查還能不能交，避免考試結束後還白跑一次評判。
    if mode == Mode::Exam {
        let state = app.state::<AppState>();
        let s = state.session.lock().map_err(err)?;
        let exam = s.exam.as_ref().ok_or("目前不在考試中")?;
        if exam.is_over(now_ms()) {
            return Err("考試時間已結束".into());
        }
    }
    let app2 = app.clone();
    let id2 = id.clone();
    let (verdict, compile_message) = blocking(move || {
        let state = app2.state::<AppState>();
        let p = load_problem(&problem_dir(&state, &id2)?).map_err(err)?;
        let cases: Vec<TestCase> = load_tests(&p, TestSet::Hidden).map_err(err)?;
        let report = cpe_judge::judge(&language(&lang)?, &source, &cases, p.time_limit(), true, &state.env);
        Ok((report.verdict, report.compile_message))
    })
    .await?;
    let now = now_ms();
    let attempts = update_session(&app, |s| -> CmdResult<usize> {
        match mode {
            Mode::Exam => {
                s.record_submission(&id, verdict, now).map_err(err)?;
                Ok(s.exam.as_ref().map_or(0, |e| e.submissions.iter().filter(|x| x.problem_id == id).count()))
            }
            Mode::Practice => {
                s.record_practice(&id, verdict, now);
                Ok(s.practice[&id].attempts as usize)
            }
        }
    })??;
    Ok(FormalResult { verdict, compile_message, attempts })
}

// ───────────── 考試狀態 ─────────────

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
struct SessionView {
    session: Session,
    /// 後端時間，前端用來校正時鐘。
    now_ms: u64,
}

#[tauri::command]
fn session_get(state: State<'_, AppState>) -> CmdResult<SessionView> {
    Ok(SessionView { session: state.session.lock().map_err(err)?.clone(), now_ms: now_ms() })
}

#[tauri::command]
fn session_agree_license(app: AppHandle) -> CmdResult<()> {
    update_session(&app, |s| s.agree_license())
}

#[tauri::command]
fn session_login(app: AppHandle, id_no: String, ticket: String, problem_ids: Vec<String>) -> CmdResult<()> {
    if id_no.trim().is_empty() || ticket.trim().is_empty() {
        return Err("請填寫身分證字號與准考碼".into());
    }
    let auth_code = format!("{:06}", now_ms() % 1_000_000);
    let examinee = Examinee { id_no: id_no.trim().into(), name: "模擬考生".into(), ticket: ticket.trim().into(), auth_code };
    app.state::<AppState>().store.clear_drafts("exam").map_err(err)?;
    update_session(&app, |s| s.login_and_start(examinee, &problem_ids, now_ms()))
}

/// 預約下一場考試的題目（考古題整場重考、預測模擬卷），並回到登入畫面。
#[tauri::command]
async fn session_plan_exam(app: AppHandle, title: String, problem_ids: Vec<String>) -> CmdResult<()> {
    if problem_ids.is_empty() {
        return Err("考卷沒有題目".into());
    }
    close_exam_windows(&app);
    app.state::<AppState>().store.clear_drafts("exam").map_err(err)?;
    update_session(&app, |s| s.plan_exam(PlannedExam { title, problem_ids }))
}

#[tauri::command]
fn session_end_exam(app: AppHandle) -> CmdResult<()> {
    update_session(&app, |s| s.end_exam(now_ms()))
}

/// 關掉所有考試的解題視窗、看題視窗與成績表。
fn close_exam_windows(app: &AppHandle) {
    for (label, w) in app.webview_windows() {
        if label.starts_with("exam-") || label.starts_with("view-") || label == "scoreboard" {
            let _ = w.close();
        }
    }
}

#[tauri::command]
async fn session_reset(app: AppHandle) -> CmdResult<()> {
    close_exam_windows(&app);
    app.state::<AppState>().store.clear_drafts("exam").map_err(err)?;
    update_session(&app, |s| s.reset_exam())
}

// ───────────── 程式碼草稿與存檔 ─────────────

#[tauri::command]
fn draft_load(state: State<'_, AppState>, scope: String, id: String) -> Option<CodeDraft> {
    state.store.load_draft(&scope, &id)
}

#[tauri::command]
fn draft_save(state: State<'_, AppState>, scope: String, draft: CodeDraft) -> CmdResult<()> {
    state.store.save_draft(&scope, &draft).map_err(err)
}

#[tauri::command]
fn saves_list(state: State<'_, AppState>) -> CmdResult<Vec<SavedCode>> {
    state.store.list_saves().map_err(err)
}

#[tauri::command]
fn save_code(state: State<'_, AppState>, name: String, draft: CodeDraft) -> CmdResult<SavedCode> {
    state.store.save_code(&name, draft, now_ms()).map_err(err)
}

// ───────────── 視窗 ─────────────

/// 開啟（或叫回）一題的解題視窗。考場上每題都是獨立視窗。
#[tauri::command]
async fn open_solve_window(app: AppHandle, mode: String, id: String, title: String) -> CmdResult<()> {
    if !["exam", "practice", "view"].contains(&mode.as_str()) {
        return Err(format!("未知的模式：{mode}"));
    }
    let label = format!("{mode}-{id}");
    open_window(&app, &label, &format!("index.html#/solve/{mode}/{id}"), &title, (1280.0, 820.0))
}

/// 開啟成績表、練習區、C++ 參考資料等輔助視窗。
#[tauri::command]
async fn open_tool_window(app: AppHandle, kind: String, title: String) -> CmdResult<()> {
    if kind == "cppref" {
        // 考場的「C++參考資料」是網站形式；外部網頁無法放自繪標題列，所以用系統原生外框
        if let Some(w) = app.get_webview_window("cppref") {
            let _ = w.unminimize();
            return w.set_focus().map_err(err);
        }
        let url = "https://en.cppreference.com/w/".parse().map_err(err)?;
        WebviewWindowBuilder::new(&app, "cppref", WebviewUrl::External(url))
            .title(title)
            .inner_size(1100.0, 760.0)
            .build()
            .map_err(err)?;
        return Ok(());
    }
    let size = match kind.as_str() {
        "scoreboard" => (1200.0, 640.0),
        "practice" => (1000.0, 760.0),
        _ => return Err(format!("未知的視窗：{kind}")),
    };
    open_window(&app, &kind, &format!("index.html#/{kind}"), &title, size)
}

fn open_window(app: &AppHandle, label: &str, url: &str, title: &str, size: (f64, f64)) -> CmdResult<()> {
    if let Some(w) = app.get_webview_window(label) {
        let _ = w.unminimize();
        let _ = w.show();
        return w.set_focus().map_err(err);
    }
    WebviewWindowBuilder::new(app, label, WebviewUrl::App(url.into()))
        .title(title)
        .inner_size(size.0, size.1)
        .min_inner_size(640.0, 400.0)
        .decorations(false)
        .build()
        .map_err(err)?;
    Ok(())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let resources = app.path().resource_dir()?;
            let data_dir = app.path().app_data_dir()?;
            let store = Store::new(data_dir.clone())?;
            let statements = StatementCache::new(data_dir.join("statements"))?;
            let session = store.load_session();
            app.manage(AppState {
                problems_dir: resources.join("problems"),
                env: JudgeEnv {
                    shim_dir: resources.join("shim"),
                    extra_paths: toolchain::default_extra_paths(),
                    compile_timeout: Duration::from_secs(30),
                },
                store,
                statements,
                session: Mutex::new(session),
                reference: Mutex::new(HashMap::new()),
            });
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            toolchain_status,
            install_command_line_tools,
            languages,
            problems,
            problem,
            problem_pdf,
            run_tests,
            run_custom,
            formal_judge,
            session_get,
            session_agree_license,
            session_login,
            session_plan_exam,
            session_end_exam,
            session_reset,
            draft_load,
            draft_save,
            saves_list,
            save_code,
            open_solve_window,
            open_tool_window
        ])
        .run(tauri::generate_context!())
        .expect("啟動 CPE 模擬考場時發生錯誤");
}
