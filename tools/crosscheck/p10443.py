"""UVa 10443 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


WINS = {"R": "S", "S": "P", "P": "R"}  # 左邊打敗右邊

def solve(s: str) -> str:
    tok = s.split()
    p, blocks = 1, []
    for _ in range(int(tok[0])):
        r, c, n = int(tok[p]), int(tok[p + 1]), int(tok[p + 2])
        g = [list(row) for row in tok[p + 3:p + 3 + r]]
        p += 3 + r
        for _ in range(n):
            new = [row[:] for row in g]
            for i in range(r):
                for j in range(c):
                    for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= a < r and 0 <= b < c and WINS[g[a][b]] == g[i][j]:
                            new[i][j] = g[a][b]
            g = new
        blocks.append("".join("".join(row) + "\n" for row in g))
    return "\n".join(blocks)
