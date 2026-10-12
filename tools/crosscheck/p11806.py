"""UVa 11806 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import combinations
from math import comb

MOD = 1000007

def brute(m, n, k):
    cells = [(i, j) for i in range(m) for j in range(n)]
    total = 0
    for pick in combinations(cells, k):
        rows = {i for i, _ in pick}; cols = {j for _, j in pick}
        total += 0 in rows and m - 1 in rows and 0 in cols and n - 1 in cols
    return total

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(v[0]):
        m, n, k = v[1 + 3 * i:4 + 3 * i]
        # 排容（另外寫一次）：沒人的邊界列數 a、行數 b
        ans = 0
        for a in range(3):
            for b in range(3):
                ways = comb(2, a) * comb(2, b)
                ans += (-1) ** (a + b) * ways * comb(max(0, (m - a) * (n - b)), k)
        if m * n <= 12:
            assert ans == brute(m, n, k)
        res.append(f"Case {i + 1}: {ans % MOD}")
    return "\n".join(res) + "\n"
