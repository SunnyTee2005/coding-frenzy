"""UVa 11806 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11806-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(1, 50)):
    m, n = rng.randint(2, 20), rng.randint(2, 20)
    if k < 4:
        m, n = rng.randint(2, 4), rng.randint(2, 4)
    qs.append((m, n, rng.randint(0, min(500, m * n))))
if kind == "hidden" and k == 1:
    qs = [(2, 2, 0), (2, 2, 4), (20, 20, 400), (20, 20, 2), (20, 20, 3), (2, 20, 2)]
out(f"{len(qs)}\n" + "".join(f"{m} {n} {kk}\n" for m, n, kk in qs))
