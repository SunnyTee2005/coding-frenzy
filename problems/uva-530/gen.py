"""UVa 530 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"530-{kind}-{k}")
out = sys.stdout.write

from math import comb
pairs = []
while len(pairs) < rng.randint(3, 60):
    n = rng.randint(1, 2**31 - 1 if rng.random() < 0.3 else 60)
    k2 = rng.randint(0, n) if n < 70 else rng.choice([0, 1, 2, n - 1, n, n - 2])
    if comb(n, k2) < 2**31:
        pairs.append((n, k2))
if kind == "hidden" and k == 1:
    pairs = [(1, 0), (1, 1), (2, 1), (33, 16), (34, 17), (2**31 - 1, 1), (2**31 - 1, 2**31 - 2), (100000, 1)]
out("".join(f"{a} {b}\n" for a, b in pairs) + "0 0\n")
