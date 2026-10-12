"""UVa 10365 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10365-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 1000) for _ in range(rng.randint(3, 100))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 997, 1000, 999, 512, 64, 720, 840]
out(f"{len(xs)}\n" + "".join(f"{x}\n" for x in xs))
