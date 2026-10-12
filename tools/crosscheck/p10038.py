"""UVa 10038 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for line in s.split("\n"):
        v = list(map(int, line.split()))
        if not v:
            continue
        n, a = v[0], v[1:1 + v[0]]
        diffs = {abs(x - y) for x, y in zip(a, a[1:])}
        res.append("Jolly" if diffs == set(range(1, n)) else "Not jolly")
    return "\n".join(res) + "\n"
