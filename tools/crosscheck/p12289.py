"""UVa 12289 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    res = []
    for w in t[1:1 + int(t[0])]:
        if len(w) == 5:
            res.append("3")
        else:
            res.append("1" if sum(a == b for a, b in zip(w, "one")) >= 2 else "2")
    return "\n".join(res) + "\n"
