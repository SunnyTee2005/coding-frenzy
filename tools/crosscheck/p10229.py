"""UVa 10229 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def fib_pair(n, mod):
    # 快速倍增法：回傳 (F(n), F(n+1)) mod
    if n == 0:
        return 0, 1 % mod
    a, b = fib_pair(n // 2, mod)
    c = a * (2 * b - a) % mod
    d = (a * a + b * b) % mod
    return (d, (c + d) % mod) if n % 2 else (c, d)

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    return "".join(f"{fib_pair(n, 1 << m)[0] % (1 << m)}\n" for n, m in zip(v[0::2], v[1::2]))
