"""UVa 100 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    cache = {1: 1}
    def cycle(n):
        path = []
        while n not in cache:
            path.append(n)
            n = 3 * n + 1 if n % 2 else n // 2
        c = cache[n]
        for x in reversed(path):
            c += 1
            cache[x] = c
        return cache[path[0]] if path else cache[n]
    res = []
    for a, b in zip(t[::2], t[1::2]):
        lo, hi = min(a, b), max(a, b)
        res.append(f"{a} {b} {max(cycle(n) for n in range(lo, hi + 1))}")
    return "\n".join(res) + "\n"
