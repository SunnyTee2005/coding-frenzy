"""UVa 10721 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10721-{kind}-{k}")
out = sys.stdout.write

qs = [(rng.randint(1, 50), rng.randint(1, 50), rng.randint(1, 50)) for _ in range(rng.randint(5, 200))]
qs = [(n, kk, m) for n, kk, m in qs if kk <= n or rng.random() < 0.1]
if kind == "hidden" and k == 1:
    qs = [(1, 1, 1), (50, 50, 1), (50, 25, 50), (50, 1, 50), (50, 1, 49), (49, 25, 3)]
out("".join(f"{n} {kk} {m}\n" for n, kk, m in qs))
