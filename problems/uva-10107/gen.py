"""UVa 10107 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10107-{kind}-{k}")
out = sys.stdout.write

n = rng.randint(1, 2000 if k > 5 else 50)
big = rng.random() < 0.5
xs = [rng.randint(0, 2**31 - 1) if big else rng.randint(0, 100) for _ in range(n)]
if kind == "hidden" and k == 1:
    xs = [2**31 - 1, 2**31 - 1, 2**31 - 2, 0, 1, 2]
out("".join(f"{x}\n" for x in xs))
