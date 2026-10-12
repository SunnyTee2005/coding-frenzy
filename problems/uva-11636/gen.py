"""UVa 11636 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11636-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 10000) if rng.random() < 0.6 else rng.randint(1, 70) for _ in range(rng.randint(5, 300))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 3, 4, 5, 1024, 1025, 8192, 8193, 10000]
out("".join(f"{x}\n" for x in xs) + f"{-rng.randint(1, 5)}\n")
