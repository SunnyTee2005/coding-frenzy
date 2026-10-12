"""UVa 12455 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        n, p = next(it), next(it)
        reach = {0}
        for _ in range(p):
            x = next(it)
            reach |= {r + x for r in reach if r + x <= n}
        res.append("YES" if n in reach else "NO")
    return "\n".join(res) + "\n"
