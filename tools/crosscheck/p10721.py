"""UVa 10721 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from functools import lru_cache

@lru_cache(maxsize=None)
def count(n, k, m):
    # 第一條寬 w（1..m），剩下 n-w 單位、k-1 條
    if k == 0:
        return 1 if n == 0 else 0
    return sum(count(n - w, k - 1, m) for w in range(1, min(m, n) + 1))

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    return "".join(f"{count(n, k, m)}\n" for n, k, m in zip(v[0::3], v[1::3], v[2::3]))
