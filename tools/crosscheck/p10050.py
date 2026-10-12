"""UVa 10050 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        n, p = next(it), next(it)
        days = set()
        for _ in range(p):
            h = next(it)
            days.update(range(h, n + 1, h))
        res.append(str(sum(1 for d in days if d % 7 not in (6, 0))))
    return "\n".join(res) + "\n"
