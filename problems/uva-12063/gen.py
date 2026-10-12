"""UVa 12063 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12063-{kind}-{k}")
out = sys.stdout.write

qs = [(rng.randint(1, 64), rng.randint(1, 100)) for _ in range(rng.randint(1, 100))]
if kind == "hidden" and k == 1:
    qs = [(1, 1), (2, 1), (2, 2), (2, 3), (64, 1), (64, 100), (63, 1), (64, 97)]
out(f"{len(qs)}\n" + "".join(f"{n} {kk}\n" for n, kk in qs))
