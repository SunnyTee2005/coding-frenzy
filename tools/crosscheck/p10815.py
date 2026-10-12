"""UVa 10815 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import re

def solve(s: str) -> str:
    words = sorted({w.lower() for w in re.findall(r"[A-Za-z]+", s)})
    return "".join(w + "\n" for w in words)
