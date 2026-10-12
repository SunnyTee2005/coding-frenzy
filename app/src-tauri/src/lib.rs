//! Tauri 後端：把判題核心（cpe-judge）包成前端可以呼叫的 command。
//!
//! 編譯與執行都是阻塞操作，一律丟到 blocking 執行緒，避免卡住 UI。

use cpe_judge::{
    builtin_languages, judge, list_problems, load_problem, load_tests, toolchain, JudgeEnv, JudgeReport, Language,
    ProblemMeta, TestSet, Verdict,
};
use serde::Serialize;
use std::path::PathBuf;
use std::time::Duration;
use tauri::{Manager, State};

struct AppState {
    problems_dir: PathBuf,
    env: JudgeEnv,
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

#[tauri::command]
fn problems(state: State<'_, AppState>) -> CmdResult<Vec<ProblemMeta>> {
    Ok(list_problems(&state.problems_dir).map_err(err)?.into_iter().map(|p| p.meta).collect())
}

#[derive(Serialize)]
struct SampleCase {
    input: String,
    output: String,
}

#[derive(Serialize)]
struct ProblemDetail {
    meta: ProblemMeta,
    statement: String,
    samples: Vec<SampleCase>,
}

fn problem_dir(state: &AppState, id: &str) -> CmdResult<PathBuf> {
    if !id.chars().all(|c| c.is_ascii_alphanumeric() || c == '-') {
        return Err(format!("題號格式錯誤：{id}"));
    }
    Ok(state.problems_dir.join(format!("uva-{id}")))
}

#[tauri::command]
fn problem(state: State<'_, AppState>, id: String) -> CmdResult<ProblemDetail> {
    let p = load_problem(&problem_dir(&state, &id)?).map_err(err)?;
    let samples = load_tests(&p, TestSet::Sample)
        .map_err(err)?
        .into_iter()
        .map(|c| SampleCase {
            input: String::from_utf8_lossy(&c.input).into_owned(),
            output: String::from_utf8_lossy(&c.output).into_owned(),
        })
        .collect();
    Ok(ProblemDetail { meta: p.meta, statement: p.statement, samples })
}

/// 測試（不列入成績）：用題目預設測試資料（sample）或人工公開測試資料（public）。
#[tauri::command]
async fn run_tests(state: State<'_, AppState>, id: String, lang: String, source: String, set: TestSet) -> CmdResult<JudgeReport> {
    if set == TestSet::Hidden {
        return Err("暗中測試資料只能用於正式評判".into());
    }
    let dir = problem_dir(&state, &id)?;
    let env = state.env.clone();
    blocking(move || {
        let p = load_problem(&dir).map_err(err)?;
        let cases = load_tests(&p, set).map_err(err)?;
        Ok(judge(&language(&lang)?, &source, &cases, p.time_limit(), false, &env))
    })
    .await
}

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
struct CustomRun {
    compile_message: Option<String>,
    status: Option<cpe_judge::ProcStatus>,
    stdout: String,
    stderr: String,
    time_ms: u64,
}

/// 自訂測試資料：只執行、不比對。
#[tauri::command]
async fn run_custom(state: State<'_, AppState>, id: String, lang: String, source: String, input: String) -> CmdResult<CustomRun> {
    let dir = problem_dir(&state, &id)?;
    let env = state.env.clone();
    blocking(move || {
        let p = load_problem(&dir).map_err(err)?;
        let compiled = match cpe_judge::compile(&language(&lang)?, &source, &env) {
            Ok(c) => c,
            Err(e) => {
                return Ok(CustomRun { compile_message: Some(e.message), status: None, stdout: String::new(), stderr: String::new(), time_ms: 0 })
            }
        };
        let out = compiled.run(input.as_bytes(), p.time_limit()).map_err(err)?;
        Ok(CustomRun {
            compile_message: None,
            status: Some(out.status),
            stdout: String::from_utf8_lossy(&out.stdout).into_owned(),
            stderr: String::from_utf8_lossy(&out.stderr).into_owned(),
            time_ms: out.elapsed.as_millis() as u64,
        })
    })
    .await
}

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
struct FormalResult {
    verdict: Verdict,
    compile_message: Option<String>,
    time_ms: u64,
}

/// 正式評判：用暗中測試資料，遇到第一筆錯誤就停；只回傳結果，不洩漏測資內容。
#[tauri::command]
async fn formal_judge(state: State<'_, AppState>, id: String, lang: String, source: String) -> CmdResult<FormalResult> {
    let dir = problem_dir(&state, &id)?;
    let env = state.env.clone();
    blocking(move || {
        let p = load_problem(&dir).map_err(err)?;
        let cases = load_tests(&p, TestSet::Hidden).map_err(err)?;
        let report = judge(&language(&lang)?, &source, &cases, p.time_limit(), true, &env);
        let time_ms = report.cases.iter().map(|c| c.time_ms).max().unwrap_or(0);
        Ok(FormalResult { verdict: report.verdict, compile_message: report.compile_message, time_ms })
    })
    .await
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let resources = app.path().resource_dir()?;
            app.manage(AppState {
                problems_dir: resources.join("problems"),
                env: JudgeEnv {
                    shim_dir: resources.join("shim"),
                    extra_paths: toolchain::default_extra_paths(),
                    compile_timeout: Duration::from_secs(30),
                },
            });
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            toolchain_status,
            install_command_line_tools,
            languages,
            problems,
            problem,
            run_tests,
            run_custom,
            formal_judge
        ])
        .run(tauri::generate_context!())
        .expect("啟動 CPE 模擬考場時發生錯誤");
}
