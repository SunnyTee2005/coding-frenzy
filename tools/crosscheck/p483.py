"""UVa 483 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import re

def solve(s: str) -> str:
    return "".join(re.sub(r"[^ ]+", lambda m: m.group(0)[::-1], line) + "\n" for line in s.split("\n")[:-1])
