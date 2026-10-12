#!/usr/bin/env python3
"""用每題的 gen.py 產生 public/hidden 測資輸入，再用 sol.cpp 算出答案。

用法：python3 tools/build_tests.py [題號...]   （不給題號就處理全部）

sample/*.in 是題目原文的範例輸入；對應的 .out 不存在時由 sol.cpp 算出（已存在的不覆蓋）。
產生完請再跑 `cargo run -p cpe-judge -- verify problems` 驗證。
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
SHIM = ROOT / "crates" / "judge" / "shim"
CXX = shutil.which("g++") or shutil.which("clang++")


def build(problem: pathlib.Path) -> None:
    meta = tomllib.loads((problem / "meta.toml").read_text(encoding="utf-8"))
    counts = meta.get("tests", {})
    gen = problem / "gen.py"
    if not gen.is_file():
        print(f"skip  {problem.name}（沒有 gen.py）")
        return
    with tempfile.TemporaryDirectory() as tmp:
        exe = pathlib.Path(tmp) / "sol"
        subprocess.run(
            [CXX, "-std=gnu++14", "-O2", "-idirafter", str(SHIM), "-o", str(exe), str(problem / "sol.cpp"), "-lm"],
            check=True,
        )
        total = 0
        for inp in sorted((problem / "sample").glob("*.in")):
            out = inp.with_suffix(".out")
            if not out.exists():
                out.write_bytes(subprocess.run([str(exe)], input=inp.read_bytes(), check=True, capture_output=True, timeout=60).stdout)
        for kind in ("public", "hidden"):
            out_dir = problem / kind
            if out_dir.exists():
                shutil.rmtree(out_dir)
            out_dir.mkdir()
            for k in range(1, counts.get(kind, 0) + 1):
                data = subprocess.run(
                    [sys.executable, "-I", str(gen), kind, str(k)], check=True, capture_output=True
                ).stdout
                answer = subprocess.run([str(exe)], input=data, check=True, capture_output=True, timeout=60).stdout
                (out_dir / f"{k}.in").write_bytes(data)
                (out_dir / f"{k}.out").write_bytes(answer)
                total += 1
    print(f"built {problem.name}：{total} 筆")


def main() -> None:
    wanted = set(sys.argv[1:])
    for problem in sorted(PROBLEMS.iterdir()):
        if (problem / "meta.toml").is_file() and (not wanted or problem.name.removeprefix("uva-") in wanted):
            build(problem)


if __name__ == "__main__":
    main()
