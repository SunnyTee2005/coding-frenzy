"""UVa 1118 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1118-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(5, 300)):
    n = rng.choice([rng.randint(1, 30), rng.randint(1, 1000000000)])
    qs.append((n, rng.choice([rng.randint(1, n), rng.randint(1, min(n, 30))])))
if kind == "hidden" and k == 1:
    qs = [(1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (1000000000, 1), (1000000000, 1000000000), (1000000000, 999999999)]
out(f"{len(qs)}\n" + "".join(f"{n} {m}\n" for n, m in qs))
