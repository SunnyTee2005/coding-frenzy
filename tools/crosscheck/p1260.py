"""UVa 1260 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import bisect

def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        n = next(it)
        seen, total = [], 0
        for _ in range(n):
            x = next(it)
            total += bisect.bisect_right(seen, x)
            bisect.insort(seen, x)
        res.append(str(total))
    return "\n".join(res) + "\n"
