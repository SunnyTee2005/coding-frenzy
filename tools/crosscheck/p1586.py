"""UVa 1586 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import re
from decimal import Decimal

def solve(s: str) -> str:
    w = {"C": Decimal("12.01"), "H": Decimal("1.008"), "O": Decimal("16.00"), "N": Decimal("14.01")}
    t = s.split()
    res = []
    for f in t[1:1 + int(t[0])]:
        total = sum(w[e] * int(n or 1) for e, n in re.findall(r"([CHON])(\d*)", f))
        res.append(f"{total:.3f}")
    return "\n".join(res) + "\n"
