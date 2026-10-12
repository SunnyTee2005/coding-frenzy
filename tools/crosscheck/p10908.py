"""UVa 10908 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    p = 0
    def nxt():
        nonlocal p
        p += 1
        return tok[p - 1]
    res = []
    for _ in range(int(nxt())):
        m, n, q = int(nxt()), int(nxt()), int(nxt())
        g = [nxt() for _ in range(m)]
        res.append(f"{m} {n} {q}")
        for _ in range(q):
            r, c = int(nxt()), int(nxt())
            best = 0
            for h in range(0, min(r, c, m - 1 - r, n - 1 - c) + 1):
                if all(g[i][c - h:c + h + 1] == g[r][c] * (2 * h + 1) for i in range(r - h, r + h + 1)):
                    best = h
                else:
                    break
            res.append(str(2 * best + 1))
    return "\n".join(res) + "\n"
