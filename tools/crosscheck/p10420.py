"""UVa 10420 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    lines = s.split("\n")
    c = Counter(line.split()[0] for line in lines[1:1 + int(lines[0])])
    return "".join(f"{k} {v}\n" for k, v in sorted(c.items()))
