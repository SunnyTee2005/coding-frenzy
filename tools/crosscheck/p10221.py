"""UVa 10221 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import math

def solve(s: str) -> str:
    tok = s.split()
    res = []
    for i in range(0, len(tok), 3):
        h, a, u = float(tok[i]), float(tok[i + 1]), tok[i + 2]
        if u == "min":
            a /= 60
        r, th = 6440 + h, a * math.acos(-1.0) / 180
        res.append(f"{r * th:.6f} {2 * r * math.sin(th / 2):.6f}")
    return "\n".join(res) + "\n"
