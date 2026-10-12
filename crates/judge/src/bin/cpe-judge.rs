//! 題庫維護用的命令列工具。
//!
//!   cpe-judge toolchains                         列出可用的編譯器
//!   cpe-judge verify <題庫目錄> [題號...]         用 sol.cpp 驗證所有測資都是 CORRECT
//!   cpe-judge judge <題目目錄> <原始檔> [--set sample|public|hidden]
//!                                                評判一份程式（語言依副檔名判斷）

use cpe_judge::{builtin_languages, judge, list_problems, load_problem, load_tests, toolchain, JudgeEnv, Language, Problem, TestSet, Verdict};
use std::path::Path;
use std::process::ExitCode;

fn main() -> ExitCode {
    let args: Vec<String> = std::env::args().skip(1).collect();
    let result = match args.first().map(String::as_str) {
        Some("toolchains") => toolchains(),
        Some("verify") if args.len() >= 2 => verify(Path::new(&args[1]), &args[2..]),
        Some("judge") if args.len() >= 3 => judge_file(&args[1..]),
        _ => {
            eprintln!("用法：cpe-judge toolchains | verify <題庫目錄> [題號...] | judge <題目目錄> <原始檔> [--set 測資組]");
            return ExitCode::from(2);
        }
    };
    match result {
        Ok(true) => ExitCode::SUCCESS,
        Ok(false) => ExitCode::FAILURE,
        Err(e) => {
            eprintln!("錯誤：{e}");
            ExitCode::from(2)
        }
    }
}

type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

fn toolchains() -> Result<bool> {
    let env = JudgeEnv::default();
    if !toolchain::command_line_tools_installed() {
        println!("（Xcode Command Line Tools 尚未安裝）");
    }
    for s in toolchain::detect(&builtin_languages(), &env.extra_paths) {
        match s.program {
            Some(p) => println!("{:<10} {}  {}", s.display, p.display(), s.version.unwrap_or_default()),
            None => println!("{:<10} （找不到）", s.display),
        }
    }
    Ok(true)
}

fn language_for(path: &Path) -> Result<Language> {
    let ext = path.extension().and_then(|e| e.to_str()).unwrap_or_default();
    builtin_languages()
        .into_iter()
        .find(|l| Path::new(&l.source).extension().and_then(|e| e.to_str()) == Some(ext))
        .ok_or_else(|| format!("無法由副檔名 .{ext} 判斷語言").into())
}

fn all_tests(problem: &Problem) -> Result<Vec<cpe_judge::TestCase>> {
    let mut cases = Vec::new();
    for set in TestSet::ALL {
        cases.extend(load_tests(problem, set)?);
    }
    Ok(cases)
}

fn verify(root: &Path, only: &[String]) -> Result<bool> {
    let env = JudgeEnv::default();
    let mut ok = true;
    for problem in list_problems(root)? {
        if !only.is_empty() && !only.contains(&problem.meta.id) {
            continue;
        }
        let sol = problem.dir.join("sol.cpp");
        let cases = all_tests(&problem)?;
        let mut problems_found = Vec::new();
        if !sol.is_file() {
            problems_found.push("缺少 sol.cpp".to_string());
        }
        for set in TestSet::ALL {
            if load_tests(&problem, set)?.is_empty() {
                problems_found.push(format!("{} 沒有測資", set.dir_name()));
            }
        }
        if sol.is_file() {
            let report = judge(&language_for(&sol)?, &std::fs::read_to_string(&sol)?, &cases, problem.time_limit(), false, &env);
            if let Some(msg) = &report.compile_message {
                problems_found.push(format!("sol.cpp 編譯失敗：\n{msg}"));
            }
            for c in report.cases.iter().filter(|c| c.verdict != Verdict::Correct) {
                problems_found.push(format!("{}：{}", c.name, c.verdict));
            }
            let slowest = report.cases.iter().map(|c| c.time_ms).max().unwrap_or(0);
            if problems_found.is_empty() {
                println!("OK    {:<8} {} 筆測資，最慢 {slowest} ms", problem.meta.id, cases.len());
                continue;
            }
        }
        ok = false;
        println!("FAIL  {:<8}", problem.meta.id);
        for p in problems_found {
            println!("      - {p}");
        }
    }
    Ok(ok)
}

fn judge_file(args: &[String]) -> Result<bool> {
    let problem = load_problem(Path::new(&args[0]))?;
    let source_path = Path::new(&args[1]);
    let cases = match args.iter().position(|a| a == "--set") {
        Some(i) => {
            let set = match args.get(i + 1).map(String::as_str) {
                Some("sample") => TestSet::Sample,
                Some("public") => TestSet::Public,
                Some("hidden") => TestSet::Hidden,
                other => return Err(format!("未知的測資組：{other:?}").into()),
            };
            load_tests(&problem, set)?
        }
        None => all_tests(&problem)?,
    };
    let report = judge(
        &language_for(source_path)?,
        &std::fs::read_to_string(source_path)?,
        &cases,
        problem.time_limit(),
        false,
        &JudgeEnv::default(),
    );
    if let Some(msg) = &report.compile_message {
        println!("{msg}");
    }
    for c in &report.cases {
        println!("{:<12} {:<20} {:>5} ms", c.name, c.verdict.as_str(), c.time_ms);
    }
    println!("結果：{}", report.verdict);
    Ok(report.verdict == Verdict::Correct)
}
