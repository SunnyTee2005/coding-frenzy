"""UVa 10539 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10539-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(1, 200)):
    hi = rng.choice([100, 10**6, 10**12 - 1])
    a = rng.randint(1, hi); b = rng.randint(a, hi)
    qs.append((a, b))
if kind == "hidden" and k == 1:
    qs = [(1, 1), (4, 4), (1, 999999999999), (999999000000, 999999999999), (2, 3), (999966000289, 999966000289)]
out(f"{len(qs)}\n" + "".join(f"{a} {b}\n" for a, b in qs))
