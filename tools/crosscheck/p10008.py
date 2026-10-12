"""UVa 10008 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    lines = s.split("\n")
    n = int(lines[0])
    c = Counter(ch.upper() for line in lines[1:1 + n] for ch in line if ch.isascii() and ch.isalpha())
    return "".join(f"{ch} {v}\n" for ch, v in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))
