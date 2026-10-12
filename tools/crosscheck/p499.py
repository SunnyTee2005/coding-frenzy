"""UVa 499 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    res = []
    for line in s.split("\n")[:-1]:
        c = Counter(ch for ch in line if ch.isascii() and ch.isalpha())
        best = max(c.values())
        res.append("".join(sorted(ch for ch, v in c.items() if v == best)) + f" {best}")
    return "".join(r + "\n" for r in res)
