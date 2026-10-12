"""UVa 496 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    res = []
    for la, lb in zip(lines[0::2], lines[1::2]):
        if not la.strip() and not lb.strip():
            continue
        a, b = set(map(int, la.split())), set(map(int, lb.split()))
        if a == b:
            res.append("A equals B")
        elif a < b:
            res.append("A is a proper subset of B")
        elif b < a:
            res.append("B is a proper subset of A")
        elif not a & b:
            res.append("A and B are disjoint")
        else:
            res.append("I'm confused!")
    return "\n".join(res) + "\n"
