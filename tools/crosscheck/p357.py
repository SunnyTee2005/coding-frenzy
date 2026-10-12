"""UVa 357 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def brute(n):
    # 直接列舉 50、25、10、5 分的枚數，剩下用 1 分補
    return sum(1 for a in range(n // 50 + 1) for b in range((n - 50 * a) // 25 + 1)
               for c in range((n - 50 * a - 25 * b) // 10 + 1) for d in range((n - 50 * a - 25 * b - 10 * c) // 5 + 1))

def solve(s: str) -> str:
    xs = list(map(int, s.split()))
    top = max(xs)
    ways = [1] + [0] * top
    for c in (50, 25, 10, 5, 1):
        for v in range(c, top + 1):
            ways[v] += ways[v - c]
    res = []
    for n in xs:
        m = ways[n]
        if n <= 120:
            assert m == brute(n)
        res.append(f"There is only 1 way to produce {n} cents change." if m == 1 else f"There are {m} ways to produce {n} cents change.")
    return "\n".join(res) + "\n"
