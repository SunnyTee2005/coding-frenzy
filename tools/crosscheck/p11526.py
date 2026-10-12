"""UVa 11526 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from math import isqrt

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for n in v[1:1 + v[0]]:
        if n <= 0:
            res.append("0")
            continue
        r = isqrt(n)
        # 數格點：xy <= n 的正整數點數 = 2 * sum_{i<=r} n//i - r^2
        res.append(str(2 * sum(n // i for i in range(1, r + 1)) - r * r))
    return "\n".join(res) + "\n"
