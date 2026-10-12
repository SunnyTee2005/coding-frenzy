"""UVa 11639 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    res = []
    for i in range(t[0]):
        r1 = t[1 + 8 * i:5 + 8 * i]; r2 = t[5 + 8 * i:9 + 8 * i]
        cover = [[0] * 100 for _ in range(100)]
        for x1, y1, x2, y2 in (r1, r2):
            for x in range(x1, x2):
                for y in range(y1, y2):
                    cover[x][y] += 1
        cnt = [0, 0, 0]
        for row in cover:
            for v in row:
                cnt[v] += 1
        res.append(f"Night {i + 1}: {cnt[2]} {cnt[1]} {cnt[0]}")
    return "\n".join(res) + "\n"
