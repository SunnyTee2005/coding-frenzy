"""UVa 1714 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1714-{kind}-{k}")
out = sys.stdout.write

CH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
cases = []
for _ in range(rng.randint(1, 3)):
    r, c = rng.randint(1, 8), rng.randint(1, 10)
    keys = rng.sample(CH, min(len(CH), rng.randint(1, r * c - 1))) if r * c > 1 else []
    # 用隨機擴張把格子分給各個鍵，保證每個鍵連通
    owner = [[None] * c for _ in range(r)]
    labels = keys + ["*"]
    cells = [(i, j) for i in range(r) for j in range(c)]
    rng.shuffle(cells)
    frontier = []
    for lab, (i, j) in zip(labels, cells):
        owner[i][j] = lab
        frontier.append((i, j))
    while frontier:
        i, j = frontier.pop(rng.randrange(len(frontier)))
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < r and 0 <= nj < c and owner[ni][nj] is None:
                owner[ni][nj] = owner[i][j]
                frontier.append((ni, nj))
    used = sorted({x for row in owner for x in row} - {"*"})
    if not used:
        continue
    text = "".join(rng.choice(used) for _ in range(rng.randint(1, 60 if k < 10 else 400)))
    cases.append(("\n".join("".join(row) for row in owner), r, c, text))
if not cases:
    cases = [("A*", 1, 2, "A")]
out("".join(f"{r} {c}\n{g}\n{t}\n" for g, r, c, t in cases))
