"""UVa 10696 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import sys

def solve(s: str) -> str:
    sys.setrecursionlimit(10000)
    memo = {}
    def f91(n):
        if n >= 101:
            return n - 10
        if n not in memo:
            memo[n] = f91(f91(n + 11))
        return memo[n]
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        res.append(f"f91({n}) = {f91(n)}")
    return "\n".join(res) + "\n"
