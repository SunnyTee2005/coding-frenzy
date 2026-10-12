"""新增題目的小工具：用一份規格產生 problems/uva-<id>/ 與 tools/crosscheck/p<id>.py。

用法（在批次腳本中）：

    import sys; sys.path.insert(0, "tools")
    from problem_kit import add
    add(272, "TEX Quotes", stars=1, sample="...", sol=r'''C++''', gen=r'''Python''', check=r'''Python''',
        cpe26=26011, category="輸入格式")

- sample：題目原文的範例輸入（範例輸出由 sol.cpp 算出，再由 check 交叉驗證）。
- gen：gen.py 的本體，可用變數 kind（"public" / "hidden"）、k（編號）、rng（已設好種子的 random.Random），
  把輸入寫到 stdout。
- check：獨立的 Python 解法，函式本體以 `def solve(s: str) -> str:` 為開頭。
- 題文不用寫：App 直接顯示 UVa 原文 PDF。
"""
import pathlib
import textwrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
CROSS = ROOT / "tools" / "crosscheck"

GEN_HEADER = '''"""UVa {uva} 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"{uva}-{{kind}}-{{k}}")
out = sys.stdout.write
'''


def add(
    uva: int,
    title: str,
    *,
    stars: int,
    sample: str,
    sol: str,
    gen: str,
    check: str,
    public: int = 3,
    hidden: int = 10,
    time_limit: float = 3.0,
    cpe26: int | None = None,
    category: str | None = None,
):
    d = PROBLEMS / f"uva-{uva}"
    (d / "sample").mkdir(parents=True, exist_ok=True)
    meta = [
        f'id = "{uva}"',
        f'title = "{title}"',
        f"stars = {stars}",
        f"time_limit = {time_limit}",
        f"uva = {uva}",
    ]
    if cpe26:
        meta.append(f"cpe26 = {cpe26}")
    if category:
        meta.append(f'category = "{category}"')
    meta += ["", "[tests]", f"public = {public}", f"hidden = {hidden}", ""]
    (d / "meta.toml").write_text("\n".join(meta), encoding="utf-8")
    (d / "sample" / "1.in").write_text(textwrap.dedent(sample).lstrip("\n"), encoding="utf-8")
    (d / "sol.cpp").write_text(textwrap.dedent(sol).lstrip("\n"), encoding="utf-8")
    (d / "gen.py").write_text(GEN_HEADER.format(uva=uva) + "\n" + textwrap.dedent(gen).lstrip("\n"), encoding="utf-8")
    (CROSS / f"p{uva}.py").write_text(
        f'"""UVa {uva} 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""\n\n\n'
        + textwrap.dedent(check).lstrip("\n"),
        encoding="utf-8",
    )
