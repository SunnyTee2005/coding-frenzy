"""UVa 11349 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11349-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 30)):
    n = rng.randint(1, 8)
    if kind == "hidden" and k == 10 and not cases:
        n = 100
    big = rng.random() < 0.3 and n < 100
    v = lambda: rng.randint(0, 2**32) if big else rng.randint(0, 9)
    m = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j] is None:
                m[i][j] = m[n - 1 - i][n - 1 - j] = v()
    r = rng.random()
    if r < 0.25:
        i, j = rng.randrange(n), rng.randrange(n); m[i][j] += 1
    elif r < 0.4:
        i, j = rng.randrange(n), rng.randrange(n)
        m[i][j] = m[n - 1 - i][n - 1 - j] = -rng.randint(1, 2**32)
    cases.append(m)
if kind == "hidden" and k == 1:
    cases = [[[0]], [[-1]], [[-4294967296]], [[4294967296]], [[1, 2], [2, 1]], [[1, 2], [1, 2]]]
out(f"{len(cases)}\n" + "".join(f"N = {len(m)}\n" + "".join(" ".join(map(str, r)) + "\n" for r in m) for m in cases))
