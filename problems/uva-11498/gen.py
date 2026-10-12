"""UVa 11498 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11498-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 10)):
    hi = rng.choice([3, 50, 9999])
    n, m = rng.randint(-hi, hi), rng.randint(-hi, hi)
    pts = [(rng.randint(-hi - 1, hi + 1), rng.randint(-hi - 1, hi + 1)) for _ in range(rng.randint(1, 100))]
    cases.append((n, m, pts))
if kind == "hidden" and k == 1:
    cases = [(0, 0, [(0, 0), (10000, 10000), (-10000, -10000), (10000, -10000), (-10000, 10000), (0, 5), (5, 0)])]
out("".join(f"{len(p)}\n{n} {m}\n" + "".join(f"{x} {y}\n" for x, y in p) for n, m, p in cases) + "0\n")
