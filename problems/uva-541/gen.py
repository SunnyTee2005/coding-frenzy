"""UVa 541 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"541-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(3, 12)):
    n = rng.randint(1, 12)
    if kind == "hidden" and k == 10 and not cases:
        n = 99
    m = [[0] * n for _ in range(n)]
    for _ in range(rng.randint(0, n * n)):
        i, j, p, q = rng.randrange(n), rng.randrange(n), rng.randrange(n), rng.randrange(n)
        if i != p and j != q:  # 翻轉矩形四角，保持每列每行的奇偶
            for x, y in ((i, j), (i, q), (p, j), (p, q)):
                m[x][y] ^= 1
    for _ in range(rng.choice([0, 1, 1, 1, 2, 3])):
        m[rng.randrange(n)][rng.randrange(n)] ^= 1
    cases.append(m)
if kind == "hidden" and k == 1:
    cases = [[[0]], [[1]], [[1, 1], [1, 1]], [[1, 0], [0, 0]], [[1, 1], [0, 0]]]
out("".join(f"{len(m)}\n" + "".join(" ".join(map(str, r)) + "\n" for r in m) for m in cases) + "0\n")
