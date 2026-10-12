#!/usr/bin/env python3
"""交叉驗證：用 tools/crosscheck/p<UVa>.py 的獨立解法重算每題所有測資，與 .out 比對。

用法：python3 tools/crosscheck/run.py [題號...]
沒有獨立解法的題目會列為 MISSING（不算失敗，但會統計）。
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
PROBLEMS = HERE.parent.parent / "problems"


def load(uva):
    path = HERE / f"p{uva}.py"
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"p{uva}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.solve


def main():
    wanted = set(sys.argv[1:])
    bad = missing = checked = 0
    for d in sorted(PROBLEMS.glob("uva-*")):
        uva = d.name.removeprefix("uva-")
        if wanted and uva not in wanted:
            continue
        solve = load(uva)
        if solve is None:
            print(f"MISSING {uva}")
            missing += 1
            continue
        for inp in sorted(d.glob("*/*.in")):
            got = solve(inp.read_text())
            if got != inp.with_suffix(".out").read_text():
                print(f"MISMATCH {inp.relative_to(PROBLEMS)}")
                bad += 1
            checked += 1
    print(f"checked {checked} files, {bad} mismatches, {missing} problems without cross-check")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
