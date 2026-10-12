"""UVa 729 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"729-{kind}-{k}")
out = sys.stdout.write

from math import comb
cases = []
while len(cases) < rng.randint(1, 5):
    n = rng.randint(1, 16)
    h = rng.randint(0, n)
    if comb(n, h) * (n + 1) < 12000:
        cases.append((n, h))
if kind == "hidden" and k == 1:
    cases = [(1, 0), (1, 1), (5, 0), (5, 5), (3, 1)]
out(f"{len(cases)}\n" + "".join(f"\n{n} {h}\n" for n, h in cases))
