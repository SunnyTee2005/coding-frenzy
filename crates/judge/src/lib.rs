//! CPE 模擬考場的判題核心。
//!
//! 流程：[`compile`] 把原始碼編譯到暫存目錄 → [`Compiled::run`] 以測資執行（含時間限制）
//! → [`compare`] 比對輸出得到 [`Verdict`]。[`judge`] 把整組測資串起來。
//!
//! 這個 crate 不依賴 Tauri，桌面 App 與命令列工具（`cpe-judge`）共用。

mod compare;
mod lang;
mod problem;
mod process;
pub mod toolchain;

pub use compare::compare;
pub use lang::{builtin_languages, Language};
pub use problem::{list_problems, load_problem, load_tests, Problem, ProblemMeta, TestCase, TestSet};
pub use process::{ProcLimits, ProcOutcome, ProcStatus};

use serde::Serialize;
use std::path::{Path, PathBuf};
use std::time::Duration;

/// 評判結果。字串形式沿用考場的 `WRONG-ANSWER` 這種寫法。
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
#[serde(rename_all = "SCREAMING-KEBAB-CASE")]
pub enum Verdict {
    Correct,
    WrongAnswer,
    PresentationError,
    CompilerError,
    RunError,
    NoOutput,
    // TODO(Phase 0)：確認原程式逾時的狀態字串。
    TimeLimitExceeded,
}

impl Verdict {
    pub fn as_str(self) -> &'static str {
        match self {
            Verdict::Correct => "CORRECT",
            Verdict::WrongAnswer => "WRONG-ANSWER",
            Verdict::PresentationError => "PRESENTATION-ERROR",
            Verdict::CompilerError => "COMPILER-ERROR",
            Verdict::RunError => "RUN-ERROR",
            Verdict::NoOutput => "NO-OUTPUT",
            Verdict::TimeLimitExceeded => "TIME-LIMIT-EXCEEDED",
        }
    }
}

impl std::fmt::Display for Verdict {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str(self.as_str())
    }
}

/// 編譯失敗時的訊息（給 COMPILER-ERROR 點開看）。
#[derive(Debug, Clone, Serialize)]
pub struct CompileError {
    pub message: String,
}

/// 編譯完成、可以執行的程式。暫存目錄在 drop 時刪除。
pub struct Compiled {
    dir: tempfile::TempDir,
    run_argv: Vec<String>,
}

/// 單筆測資的執行與評判結果。
#[derive(Debug, Clone, Serialize)]
pub struct CaseResult {
    pub name: String,
    pub verdict: Verdict,
    pub time_ms: u64,
    /// 最大記憶體用量（KB），平台不支援時為 None。
    pub memory_kb: Option<u64>,
    pub stdout: String,
    pub stderr: String,
    pub exit_code: Option<i32>,
}

/// 一次評判（多筆測資）的總結果。
#[derive(Debug, Clone, Serialize)]
pub struct JudgeReport {
    pub verdict: Verdict,
    pub compile_message: Option<String>,
    pub cases: Vec<CaseResult>,
}

/// 編譯與執行時需要的環境。
#[derive(Debug, Clone)]
pub struct JudgeEnv {
    /// `bits/stdc++.h` 補丁目錄（含 `bits/` 子目錄的那一層）。
    pub shim_dir: PathBuf,
    /// 額外的執行檔搜尋路徑（GUI App 的 PATH 很短，需要補上 Homebrew 等位置）。
    pub extra_paths: Vec<PathBuf>,
    pub compile_timeout: Duration,
}

impl Default for JudgeEnv {
    fn default() -> Self {
        JudgeEnv {
            shim_dir: PathBuf::from(concat!(env!("CARGO_MANIFEST_DIR"), "/shim")),
            extra_paths: toolchain::default_extra_paths(),
            compile_timeout: Duration::from_secs(30),
        }
    }
}

const EXE_NAME: &str = if cfg!(windows) { "main.exe" } else { "main" };
/// 單筆測資的輸出上限，超過視為 RUN-ERROR（避免無窮輸出塞爆硬碟）。
const OUTPUT_LIMIT: u64 = 64 * 1024 * 1024;
/// 回傳給 UI 顯示的 stdout / stderr 長度上限。
const DISPLAY_LIMIT: usize = 64 * 1024;

/// 編譯原始碼。找不到編譯器也回傳 [`CompileError`]，訊息說明缺少什麼。
pub fn compile(lang: &Language, source: &str, env: &JudgeEnv) -> Result<Compiled, CompileError> {
    let program = toolchain::resolve(lang, &env.extra_paths).ok_or_else(|| CompileError {
        message: format!(
            "找不到 {} 的編譯器或直譯器（嘗試過：{}）。",
            lang.display,
            lang.programs.join(", ")
        ),
    })?;
    let dir = tempfile::Builder::new()
        .prefix("cpe-sim-")
        .tempdir()
        .map_err(|e| CompileError { message: format!("無法建立暫存目錄：{e}") })?;
    let src = dir.path().join(&lang.source);
    std::fs::write(&src, source)
        .map_err(|e| CompileError { message: format!("無法寫入原始檔：{e}") })?;
    let exe = dir.path().join(EXE_NAME);
    let vars = Vars { cc: &program, src: &src, exe: &exe, shim: &env.shim_dir };

    if let Some(compile_argv) = &lang.compile {
        let argv = vars.expand(compile_argv);
        let limits = ProcLimits { wall: env.compile_timeout, output_bytes: OUTPUT_LIMIT };
        let out = process::run(&argv, dir.path(), None, &limits)
            .map_err(|e| CompileError { message: format!("無法執行編譯器 {}：{e}", argv[0]) })?;
        let mut message = String::from_utf8_lossy(&out.stderr).into_owned();
        message.push_str(&String::from_utf8_lossy(&out.stdout));
        match out.status {
            ProcStatus::Exited(0) => {}
            ProcStatus::TimedOut => {
                return Err(CompileError { message: format!("編譯逾時（超過 {} 秒）。", env.compile_timeout.as_secs()) })
            }
            _ => return Err(CompileError { message: truncate(message) }),
        }
    }
    Ok(Compiled { run_argv: vars.expand(&lang.run), dir })
}

impl Compiled {
    /// 以 `input` 作為標準輸入執行一次。
    pub fn run(&self, input: &[u8], time_limit: Duration) -> std::io::Result<ProcOutcome> {
        let input_path = self.dir.path().join("input.txt");
        std::fs::write(&input_path, input)?;
        // 稍微放寬牆鐘時間再強制結束，判定 TLE 時仍以 time_limit 為準。
        let limits = ProcLimits {
            wall: time_limit + Duration::from_millis(200),
            output_bytes: OUTPUT_LIMIT,
        };
        process::run(&self.run_argv, self.dir.path(), Some(&input_path), &limits)
    }

    /// 執行並與預期輸出比對。
    pub fn run_case(&self, case: &TestCase, time_limit: Duration) -> CaseResult {
        match self.run(&case.input, time_limit) {
            Ok(out) => {
                let verdict = verdict_for(&out, &case.output, time_limit);
                CaseResult {
                    name: case.name.clone(),
                    verdict,
                    time_ms: out.elapsed.as_millis() as u64,
                    memory_kb: out.max_rss_kb,
                    stdout: truncate(String::from_utf8_lossy(&out.stdout).into_owned()),
                    stderr: truncate(String::from_utf8_lossy(&out.stderr).into_owned()),
                    exit_code: match out.status {
                        ProcStatus::Exited(c) => Some(c),
                        _ => None,
                    },
                }
            }
            Err(e) => CaseResult {
                name: case.name.clone(),
                verdict: Verdict::RunError,
                time_ms: 0,
                memory_kb: None,
                stdout: String::new(),
                stderr: format!("無法執行程式：{e}"),
                exit_code: None,
            },
        }
    }
}

/// 由執行結果與預期輸出決定評判結果。
pub fn verdict_for(out: &ProcOutcome, expected: &[u8], time_limit: Duration) -> Verdict {
    match out.status {
        ProcStatus::TimedOut => Verdict::TimeLimitExceeded,
        ProcStatus::OutputLimit => Verdict::RunError,
        ProcStatus::Signaled(_) | ProcStatus::Exited(1..) | ProcStatus::Exited(..=-1) => {
            if out.cpu_exceeded {
                Verdict::TimeLimitExceeded
            } else {
                Verdict::RunError
            }
        }
        ProcStatus::Exited(0) if out.elapsed > time_limit => Verdict::TimeLimitExceeded,
        ProcStatus::Exited(_) => compare(expected, &out.stdout),
    }
}

/// 編譯並跑完整組測資。`stop_at_first_failure` 為 true 時遇到第一筆錯誤就停（正式評判用）。
pub fn judge(
    lang: &Language,
    source: &str,
    cases: &[TestCase],
    time_limit: Duration,
    stop_at_first_failure: bool,
    env: &JudgeEnv,
) -> JudgeReport {
    let compiled = match compile(lang, source, env) {
        Ok(c) => c,
        Err(e) => {
            return JudgeReport { verdict: Verdict::CompilerError, compile_message: Some(e.message), cases: vec![] }
        }
    };
    let mut results = Vec::with_capacity(cases.len());
    let mut verdict = Verdict::Correct;
    for case in cases {
        let r = compiled.run_case(case, time_limit);
        let failed = r.verdict != Verdict::Correct;
        if failed && verdict == Verdict::Correct {
            verdict = r.verdict;
        }
        results.push(r);
        if failed && stop_at_first_failure {
            break;
        }
    }
    JudgeReport { verdict, compile_message: None, cases: results }
}

struct Vars<'a> {
    cc: &'a Path,
    src: &'a Path,
    exe: &'a Path,
    shim: &'a Path,
}

impl Vars<'_> {
    fn expand(&self, template: &[String]) -> Vec<String> {
        template
            .iter()
            .map(|arg| {
                arg.replace("{cc}", &self.cc.to_string_lossy())
                    .replace("{src}", &self.src.to_string_lossy())
                    .replace("{exe}", &self.exe.to_string_lossy())
                    .replace("{shim}", &self.shim.to_string_lossy())
            })
            .collect()
    }
}

fn truncate(mut s: String) -> String {
    if s.len() > DISPLAY_LIMIT {
        let mut cut = DISPLAY_LIMIT;
        while !s.is_char_boundary(cut) {
            cut -= 1;
        }
        s.truncate(cut);
        s.push_str("\n…（輸出過長，已截斷）");
    }
    s
}
