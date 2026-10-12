"""UVa 1260 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1260-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 8)):
    n = rng.randint(2, 1000 if k == 10 else 100)
    hi = rng.choice([5, 100, 5000])
    cases.append([rng.randint(1, hi) for _ in range(n)])
if kind == "hidden" and k == 1:
    cases = [[1, 1], [2, 1], [1, 2], [5000] * 10, list(range(10, 0, -1))]
out(f"{len(cases)}\n" + "".join(f"{len(c)}\n{' '.join(map(str, c))}\n" for c in cases))
