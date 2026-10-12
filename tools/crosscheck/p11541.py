"""UVa 11541 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import re

def solve(s: str) -> str:
    t = s.split()
    res = []
    for i, enc in enumerate(t[1:1 + int(t[0])], 1):
        res.append(f"Case {i}: " + "".join(ch * int(n) for ch, n in re.findall(r"([A-Z])(\d+)", enc)))
    return "\n".join(res) + "\n"
