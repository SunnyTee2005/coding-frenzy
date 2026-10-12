"""UVa 10273 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10273-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 8)):
    n = rng.randint(1, 30 if k < 10 else 300)
    hi = rng.choice([2, 5, 250])
    cases.append([[rng.randint(0, hi) for _ in range(rng.randint(1, 10))] for _ in range(n)])
if kind == "hidden" and k == 1:
    cases = [[[5]], [[1], [1]], [[1, 2], [2, 1]], [[0] * 10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]]
out(f"{len(cases)}\n" + "".join(f"{len(c)}\n" + "".join(f"{len(m)} {' '.join(map(str, m))}\n" for m in c) for c in cases))
