"""UVa 10642 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10642-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(1, 500)):
    hi = rng.choice([5, 100, 100000])
    p = (rng.randint(0, hi), rng.randint(0, hi)); q = (rng.randint(0, hi), rng.randint(0, hi))
    if (p[0] + p[1], p[0]) > (q[0] + q[1], q[0]):
        p, q = q, p
    qs.append(p + q)
if kind == "hidden" and k == 1:
    qs = [(0, 0, 0, 0), (0, 3, 3, 0), (0, 0, 100000, 100000), (100000, 100000, 100000, 100000), (0, 100000, 100000, 0)]
out(f"{len(qs)}\n" + "".join(" ".join(map(str, q)) + "\n" for q in qs))
