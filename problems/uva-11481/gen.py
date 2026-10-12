"""UVa 11481 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11481-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(1, 100)):
    n = rng.randint(1, 1000 if rng.random() < 0.5 else 8)
    m = rng.randint(0, n)
    qs.append((n, m, rng.randint(0, m)))
if kind == "hidden" and k == 1:
    qs = [(1, 0, 0), (1, 1, 1), (1, 1, 0), (2, 2, 0), (1000, 1000, 0), (1000, 0, 0), (1000, 1000, 1000)]
out(f"{len(qs)}\n" + "".join(f"{n} {m} {kk}\n" for n, m, kk in qs))
