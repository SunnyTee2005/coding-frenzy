"""UVa 11240 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11240-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 20)):
    n = rng.randint(1, 40) if (k < 10 or cases) else 6000
    p = list(range(1, n + 1))
    r = rng.random()
    if r < 0.6:
        rng.shuffle(p)
    elif r < 0.8:
        p.reverse()
    cases.append(p)
if kind == "hidden" and k == 1:
    cases = [[1], [1, 2], [2, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3, 4]]
out(f"{len(cases)}\n" + "".join(f"{len(p)} {' '.join(map(str, p))}\n" for p in cases))
