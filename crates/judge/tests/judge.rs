//! 每種評判結果各用一支小程式驗證，需要本機有 C++ 編譯器與 python3。

use cpe_judge::{builtin_languages, judge, JudgeEnv, Language, TestCase, Verdict};
use std::time::{Duration, Instant};

fn lang(id: &str) -> Language {
    builtin_languages().into_iter().find(|l| l.id == id).unwrap()
}

fn case(input: &str, output: &str) -> TestCase {
    TestCase { name: "t".into(), input: input.into(), output: output.into() }
}

fn verdict(lang_id: &str, source: &str) -> Verdict {
    let cases = [case("3 4\n10 20\n", "7\n30\n")];
    judge(&lang(lang_id), source, &cases, Duration::from_secs(1), false, &JudgeEnv::default()).verdict
}

const CPP_OK: &str = r#"
#include <bits/stdc++.h>
using namespace std;
int main() { long long a, b; while (cin >> a >> b) cout << a + b << "\n"; }
"#;

#[test]
fn cpp_correct_with_bits_stdcxx() {
    assert_eq!(verdict("ccpp", CPP_OK), Verdict::Correct);
}

#[test]
fn c_source_compiles_as_cpp() {
    // 考場把 C 程式也存成 main.cpp 用 g++ 編譯。
    let src = "#include <stdio.h>\nint main(){long a,b;while(scanf(\"%ld %ld\",&a,&b)==2)printf(\"%ld\\n\",a+b);return 0;}\n";
    assert_eq!(verdict("ccpp", src), Verdict::Correct);
    // 合法的 C、但不是合法的 C++：考場上會 COMPILER-ERROR。
    let c_only = "#include <stdlib.h>\nint main(){int *p = malloc(4); int new = 1; return p[0] * new;}\n";
    assert_eq!(verdict("ccpp", c_only), Verdict::CompilerError);
}

#[test]
fn python_correct() {
    let src = "import sys\nfor line in sys.stdin:\n    a, b = map(int, line.split())\n    print(a + b)\n";
    assert_eq!(verdict("python", src), Verdict::Correct);
}

#[test]
fn wrong_answer() {
    let src = "#include <cstdio>\nint main(){long a,b;while(scanf(\"%ld %ld\",&a,&b)==2)printf(\"%ld\\n\",a-b);}\n";
    assert_eq!(verdict("ccpp", src), Verdict::WrongAnswer);
}

#[test]
fn presentation_error() {
    let src = "#include <cstdio>\nint main(){long a,b;while(scanf(\"%ld %ld\",&a,&b)==2)printf(\"%ld \",a+b);}\n";
    assert_eq!(verdict("ccpp", src), Verdict::PresentationError);
}

#[test]
fn no_output() {
    assert_eq!(verdict("ccpp", "int main(){}\n"), Verdict::NoOutput);
}

#[test]
fn compiler_error_keeps_message() {
    let report = judge(&lang("ccpp"), "int main( {", &[case("", "")], Duration::from_secs(1), false, &JudgeEnv::default());
    assert_eq!(report.verdict, Verdict::CompilerError);
    assert!(report.compile_message.unwrap().contains("error"));
}

#[test]
fn python_syntax_error_is_run_error() {
    // 考場的 Python 沒有編譯步驟，語法錯誤在執行時出現。
    assert_eq!(verdict("python", "print(1\n"), Verdict::RunError);
}

#[test]
fn run_error_on_crash_and_nonzero_exit() {
    let segv = "int main(){ volatile int *p = 0; *p = 1; }\n";
    assert_eq!(verdict("ccpp", segv), Verdict::RunError);
    assert_eq!(verdict("ccpp", "int main(){ return 3; }\n"), Verdict::RunError);
    assert_eq!(verdict("python", "raise SystemExit(1)\n"), Verdict::RunError);
}

#[test]
fn time_limit_kills_infinite_loop_quickly() {
    let start = Instant::now();
    assert_eq!(verdict("ccpp", "int main(){ volatile int x = 0; for(;;) x++; }\n"), Verdict::TimeLimit);
    assert!(start.elapsed() < Duration::from_secs(8), "逾時程式沒有被及時結束：{:?}", start.elapsed());
}

#[test]
fn time_limit_kills_forked_children() {
    // 程式自己開的子行程也要被一起結束，否則 judge 會被卡住。
    let src = "import os, time\nif os.fork() == 0:\n    time.sleep(60)\nelse:\n    time.sleep(60)\n";
    let start = Instant::now();
    assert_eq!(verdict("python", src), Verdict::TimeLimit);
    assert!(start.elapsed() < Duration::from_secs(8));
}

#[test]
fn stop_at_first_failure() {
    let cases = [case("1 1\n", "2\n"), case("1 2\n", "4\n"), case("2 2\n", "4\n")];
    let report = judge(&lang("ccpp"), CPP_OK, &cases, Duration::from_secs(1), true, &JudgeEnv::default());
    assert_eq!(report.verdict, Verdict::WrongAnswer);
    assert_eq!(report.cases.len(), 2);
}
