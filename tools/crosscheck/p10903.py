"""UVa 10903 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


BEATS = {("paper", "rock"), ("scissors", "paper"), ("rock", "scissors")}

def solve(s: str) -> str:
    tok = s.split()
    p, blocks = 0, []
    while tok[p] != "0":
        n, k = int(tok[p]), int(tok[p + 1])
        p += 2
        w, l = [0] * (n + 1), [0] * (n + 1)
        for _ in range(k * n * (n - 1) // 2):
            p1, m1, p2, m2 = int(tok[p]), tok[p + 1], int(tok[p + 2]), tok[p + 3]
            p += 4
            if (m1, m2) in BEATS:
                w[p1] += 1; l[p2] += 1
            elif (m2, m1) in BEATS:
                w[p2] += 1; l[p1] += 1
        blocks.append("".join(("-" if w[i] + l[i] == 0 else f"{w[i] / (w[i] + l[i]):.3f}") + "\n" for i in range(1, n + 1)))
    return "\n".join(blocks)
