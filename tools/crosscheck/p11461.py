"""UVa 11461 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from math import isqrt

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for a, b in zip(v[0::2], v[1::2]):
        if a == 0 and b == 0:
            break
        res.append(str(isqrt(b) - isqrt(a - 1)))
    return "\n".join(res) + "\n"
