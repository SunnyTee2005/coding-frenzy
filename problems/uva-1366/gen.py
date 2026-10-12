"""UVa 1366 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1366-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 5)):
    n, m = rng.randint(1, 12), rng.randint(1, 12)
    if kind == "hidden" and k == 10 and not cases:
        n, m = 60, 60
    hi = rng.choice([1, 10, 1000])
    cases.append([[[rng.randint(0, hi) for _ in range(m)] for _ in range(n)] for _ in range(2)])
if kind == "hidden" and k == 1:
    cases = [[[[5]], [[7]]], [[[0]], [[0]]], [[[1, 2]], [[3, 4]]], [[[1], [2]], [[3], [4]]]]
out("".join(f"{len(c[0])} {len(c[0][0])}\n" + "".join(" ".join(map(str, r)) + "\n" for g in c for r in g) for c in cases) + "0 0\n")
