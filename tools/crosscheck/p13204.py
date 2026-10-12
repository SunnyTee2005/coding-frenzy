"""UVa 13204 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from functools import lru_cache
from itertools import permutations

MOD = 1000000007

@lru_cache(maxsize=None)
def brute(n):
    t = n * n // 2
    return sum(1 for p in permutations(range(n)) if sum(abs(a - i) for i, a in enumerate(p)) == t)

def solve(s: str) -> str:
    xs = list(map(int, s.split()))
    # 公式（偶數 (n/2)!^2，奇數 n*((n-1)/2)!^2）先用暴力法驗證小的 n
    k = max(xs) // 2
    fact = [1] * (k + 1)
    for i in range(1, k + 1):
        fact[i] = fact[i - 1] * i % MOD
    res = []
    for n in xs:
        ans = fact[n // 2] ** 2 % MOD * (n if n % 2 else 1) % MOD
        if n <= 8:
            assert ans == brute(n)
        res.append(str(ans))
    return "\n".join(res) + "\n"
