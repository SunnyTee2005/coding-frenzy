"""UVa 10591 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10591-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 999999999) if rng.random() < 0.6 else rng.randint(1, 1000) for _ in range(rng.randint(1, 200))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 4, 7, 10, 100, 999999999, 1000000]
out(f"{len(xs)}\n" + "".join(f"{x}\n" for x in xs))
