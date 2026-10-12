"""UVa 11352 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11352-{kind}-{k}")
out = sys.stdout.write

def case():
    m, n = rng.randint(1, 100 if k == 10 else 12), rng.randint(1, 100 if k == 10 else 12)
    if m * n < 2:
        m, n = 1, 2
    cells = [["." for _ in range(n)] for _ in range(m)]
    density = rng.random() * 0.15
    for i in range(m):
        for j in range(n):
            if rng.random() < density: cells[i][j] = "Z"
    free = [(i, j) for i in range(m) for j in range(n)]
    (ai, aj), (bi, bj) = rng.sample(free, 2)
    cells[ai][aj], cells[bi][bj] = "A", "B"
    return f"{m} {n}\n" + "".join("".join(r) + "\n" for r in cells)
cases = [case() for _ in range(rng.randint(1, 6 if k != 10 else 1))]
out(f"{len(cases)}\n" + "".join(cases))
