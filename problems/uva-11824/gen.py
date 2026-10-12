"""UVa 11824 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11824-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 10)):
    n = rng.randint(1, 39)
    hi = rng.choice([3, 10, 50, 1000, 2500000])
    cases.append([rng.randint(1, hi) for _ in range(n)])
if kind == "hidden" and k == 1:
    cases = [[1], [2500000], [2500001], [1] * 39, [2, 2, 2], [1000, 1000]]
out(f"{len(cases)}\n" + "".join("".join(f"{x}\n" for x in c) + "0\n" for c in cases))
