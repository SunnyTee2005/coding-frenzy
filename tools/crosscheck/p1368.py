"""UVa 1368 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    tok = s.split()
    p, res = 1, []
    for _ in range(int(tok[0])):
        m, n = int(tok[p]), int(tok[p + 1])
        rows = tok[p + 2:p + 2 + m]
        p += 2 + m
        cons, err = [], 0
        for col in zip(*rows):
            c = Counter(col)
            ch = min(c, key=lambda x: (-c[x], x))
            cons.append(ch)
            err += m - c[ch]
        res += ["".join(cons), str(err)]
    return "\n".join(res) + "\n"
