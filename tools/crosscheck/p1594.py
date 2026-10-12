"""UVa 1594 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        n = next(it)
        a = tuple(next(it) for _ in range(n))
        seen = set()
        while any(a) and a not in seen:
            seen.add(a)
            a = tuple(abs(a[i] - a[(i + 1) % n]) for i in range(n))
        res.append("LOOP" if any(a) else "ZERO")
    return "\n".join(res) + "\n"
