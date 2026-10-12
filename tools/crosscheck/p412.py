"""UVa 412 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import math

def solve(s: str) -> str:
    t = list(map(int, s.split()))
    i, res = 0, []
    while t[i] != 0:
        n = t[i]; v = t[i + 1:i + 1 + n]; i += 1 + n
        pairs = n * (n - 1) // 2
        cop = sum(math.gcd(v[a], v[b]) == 1 for a in range(n) for b in range(a + 1, n))
        res.append("No estimate for this data set." if cop == 0 else f"{math.sqrt(6 * pairs / cop):.6f}")
    return "\n".join(res) + "\n"
