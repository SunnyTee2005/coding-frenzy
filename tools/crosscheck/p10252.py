"""UVa 10252 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    lines = s.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    res = []
    for a, b in zip(lines[0::2], lines[1::2]):
        common = Counter(a) & Counter(b)
        res.append("".join(sorted(common.elements())))
    return "\n".join(res) + "\n"
