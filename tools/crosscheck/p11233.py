"""UVa 11233 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    l, n = int(tok[0]), int(tok[1])
    irr = {tok[2 + 2 * i]: tok[3 + 2 * i] for i in range(l)}
    res = []
    for w in tok[2 + 2 * l:2 + 2 * l + n]:
        if w in irr:
            res.append(irr[w])
        elif len(w) >= 2 and w[-1] == "y" and w[-2] not in "aeiou":
            res.append(w[:-1] + "ies")
        elif w.endswith(("o", "s", "ch", "sh", "x")):
            res.append(w + "es")
        else:
            res.append(w + "s")
    return "\n".join(res) + "\n"
