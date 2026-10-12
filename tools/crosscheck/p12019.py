"""UVa 12019 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import datetime

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(v[0]):
        m, d = v[1 + 2 * i], v[2 + 2 * i]
        res.append(datetime.date(2011, m, d).strftime("%A"))
    return "\n".join(res) + "\n"
