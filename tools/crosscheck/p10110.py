"""UVa 10110 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from math import isqrt

def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        res.append("yes" if isqrt(n) ** 2 == n else "no")
    return "\n".join(res) + "\n"
