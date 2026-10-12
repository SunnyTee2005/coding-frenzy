"""UVa 10125 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10125-{kind}-{k}")
out = sys.stdout.write

sets = []
for _ in range(rng.randint(1, 6)):
    n = rng.randint(1, 30 if k < 10 else 300)
    hi = rng.choice([10, 1000, 536870912])
    n = min(n, 2 * hi + 1)
    vals = set()
    while len(vals) < n:
        vals.add(rng.randint(-hi, hi))
    sets.append(list(vals))
if kind == "hidden" and k == 1:
    sets = [[1], [1, 2, 3], [1, 2, 3, 6], [-1, -2, -3, -6], [0, 1, 2, 3], [-5, 0, 5, 10]]
out("".join(f"{len(s)}\n" + "".join(f"{x}\n" for x in s) for s in sets) + "0\n")
