"""UVa 10107 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import bisect

def solve(s: str) -> str:
    v, res = [], []
    for x in map(int, s.split()):
        bisect.insort(v, x)
        n = len(v)
        res.append(v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) // 2)
    return "".join(f"{r}\n" for r in res)
