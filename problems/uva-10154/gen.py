"""UVa 10154 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10154-{kind}-{k}")
out = sys.stdout.write

n = rng.randint(1, 12 if k < 6 else (2000 if k == 10 else 300))
ts = []
for _ in range(n):
    w = rng.randint(1, rng.choice([10, 1000, 100000]))
    ts.append((w, w + rng.randint(0, rng.choice([10, 1000, 1000000]))))
if kind == "hidden" and k == 1:
    ts = [(1, 1), (1, 1), (1, 2)]
out("".join(f"{w} {s}\n" for w, s in ts))
