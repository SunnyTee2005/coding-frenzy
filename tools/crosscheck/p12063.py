"""UVa 12063 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from functools import lru_cache
from itertools import combinations

def count(n, k):
    if n % 2:
        return 0
    if n <= 16:  # 小的直接列舉
        total = 0
        for ones in combinations(range(n - 1), n // 2 - 1):
            x = 1 << (n - 1)
            for b in ones:
                x |= 1 << b
            total += x % k == 0
        return total

    @lru_cache(maxsize=None)
    def f(pos, ones_left, rem):
        # 從高位往低位決定剩下 pos 個位元
        if pos == 0:
            return 1 if ones_left == 0 and rem == 0 else 0
        if ones_left > pos:
            return 0
        r = f(pos - 1, ones_left, rem * 2 % k)
        if ones_left:
            r += f(pos - 1, ones_left - 1, (rem * 2 + 1) % k)
        return r
    return f(n - 1, n // 2 - 1, 1 % k)

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    return "".join(f"Case {i + 1}: {count(v[1 + 2 * i], v[2 + 2 * i])}\n" for i in range(v[0]))
