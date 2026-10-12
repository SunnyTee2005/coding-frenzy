"""UVa 512 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    p, blocks, cs = 0, [], 0
    while True:
        r, c = map(int, lines[p].split()); p += 1
        if r == 0 and c == 0:
            break
        cs += 1
        # 整張表模擬：每格放原本的座標，None 表示插入的空格
        grid = [[(i, j) for j in range(1, c + 1)] for i in range(1, r + 1)]
        n = int(lines[p]); p += 1
        for _ in range(n):
            t = lines[p].split(); p += 1
            if t[0] == "EX":
                r1, c1, r2, c2 = map(int, t[1:])
                grid[r1 - 1][c1 - 1], grid[r2 - 1][c2 - 1] = grid[r2 - 1][c2 - 1], grid[r1 - 1][c1 - 1]
                continue
            labels = set(map(int, t[2:2 + int(t[1])]))
            if t[0] == "DR":
                grid = [row for i, row in enumerate(grid, 1) if i not in labels]
            elif t[0] == "DC":
                grid = [[x for j, x in enumerate(row, 1) if j not in labels] for row in grid]
            elif t[0] == "IR":
                width = len(grid[0])
                new = []
                for i, row in enumerate(grid, 1):
                    if i in labels:
                        new.append([None] * width)
                    new.append(row)
                grid = new
            else:
                grid = [sum(([None, x] if j in labels else [x] for j, x in enumerate(row, 1)), []) for row in grid]
        where = {x: (i, j) for i, row in enumerate(grid, 1) for j, x in enumerate(row, 1) if x}
        q = int(lines[p]); p += 1
        out = [f"Spreadsheet #{cs}"]
        for _ in range(q):
            a, b = map(int, lines[p].split()); p += 1
            out.append(f"Cell data in ({a},{b}) moved to ({where[(a, b)][0]},{where[(a, b)][1]})" if (a, b) in where
                       else f"Cell data in ({a},{b}) GONE")
        blocks.append("".join(o + "\n" for o in out))
    return "\n".join(blocks)
