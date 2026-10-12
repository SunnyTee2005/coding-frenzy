"""UVa 10010 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    i = 1
    outs = []
    for _ in range(int(t[0])):
        m, n = int(t[i]), int(t[i + 1]); i += 2
        g = [r.lower() for r in t[i:i + m]]; i += m
        k = int(t[i]); i += 1
        lines = []
        for w in t[i:i + k]:
            w = w.lower()
            best = None
            for r in range(m):
                for c in range(n):
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if (dr, dc) == (0, 0):
                                continue
                            cells = [(r + dr * q, c + dc * q) for q in range(len(w))]
                            if all(0 <= x < m and 0 <= y < n and g[x][y] == w[q] for q, (x, y) in enumerate(cells)):
                                best = min(best or (r, c), (r, c))
            lines.append(f"{best[0] + 1} {best[1] + 1}")
        i += k
        outs.append("\n".join(lines) + "\n")
    return "\n".join(outs)
