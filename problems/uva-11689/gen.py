"""UVa 11689 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11689-{kind}-{k}")
out = sys.stdout.write

qs = [(rng.randint(0, 999), rng.randint(0, 999), rng.choice([2, 3, rng.randint(2, 1999)])) for _ in range(rng.randint(1, 14))]
if kind == "hidden" and k == 1:
    qs = [(0, 0, 2), (1, 0, 2), (999, 999, 2), (999, 999, 1999), (1, 1, 2)]
out(f"{len(qs)}\n" + "".join(f"{e} {f} {c}\n" for e, f, c in qs))
