"""UVa 1193 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1193-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 10)):
    n = rng.randint(1, 30 if k < 10 else 1000)
    d = rng.randint(1, 20)
    pts = [(rng.randint(-50, 50), rng.randint(0, d + (1 if rng.random() < 0.1 else 0))) for _ in range(n)]
    cases.append((d, pts))
if kind == "hidden" and k == 1:
    cases = [(1, [(0, 1)]), (1, [(0, 2)]), (5, [(0, 3), (8, 3)]), (5, [(0, 3), (9, 3)]), (2, [(0, 0), (4, 0)])]
out("".join(f"{len(p)} {d}\n" + "".join(f"{x} {y}\n" for x, y in p) + "\n" for d, p in cases) + "0 0\n")
