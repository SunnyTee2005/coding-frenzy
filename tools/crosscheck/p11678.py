"""UVa 11678 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    while True:
        a, b = next(it), next(it)
        if a == 0 and b == 0:
            break
        sa = {next(it) for _ in range(a)}
        sb = {next(it) for _ in range(b)}
        res.append(str(min(len(sa - sb), len(sb - sa))))
    return "\n".join(res) + "\n"
