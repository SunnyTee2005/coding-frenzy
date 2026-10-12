"""UVa 11481 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import permutations
from math import comb, factorial

MOD = 1000000007
_brute = {}

def brute(n, m, k):
    key = (n, m, k)
    if key not in _brute:
        _brute[key] = sum(1 for p in permutations(range(n)) if sum(p[i] == i for i in range(m)) == k)
    return _brute[key]

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(v[0]):
        n, m, k = v[1 + 3 * i:4 + 3 * i]
        ans = comb(m, k) * sum((-1) ** j * comb(m - k, j) * factorial(n - k - j) for j in range(m - k + 1)) % MOD
        if n <= 7:
            assert ans == brute(n, m, k)
        res.append(f"Case {i + 1}: {ans}")
    return "\n".join(res) + "\n"
