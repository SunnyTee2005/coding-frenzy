"""UVa 11624 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    p, res = 1, []
    for _ in range(int(tok[0])):
        r, c = int(tok[p]), int(tok[p + 1])
        g = tok[p + 2:p + 2 + r]
        p += 2 + r
        open_cells = {(i, j) for i in range(r) for j in range(c) if g[i][j] != "#"}
        burning = {(i, j) for i in range(r) for j in range(c) if g[i][j] == "F"}
        joe = {(i, j) for i in range(r) for j in range(c) if g[i][j] == "J"}
        seen = set(joe)
        t, ans = 0, None
        # 一分鐘一分鐘模擬：喬先看能不能從邊界走出去，再一起擴散
        while joe:
            if any(i in (0, r - 1) or j in (0, c - 1) for i, j in joe):
                ans = t + 1
                break
            t += 1
            burning = burning | {(i + di, j + dj) for i, j in burning for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1))
                                 if (i + di, j + dj) in open_cells}
            joe = {(i + di, j + dj) for i, j in joe for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1))
                   if (i + di, j + dj) in open_cells and (i + di, j + dj) not in burning and (i + di, j + dj) not in seen}
            seen |= joe
        res.append("IMPOSSIBLE" if ans is None else str(ans))
    return "\n".join(res) + "\n"
