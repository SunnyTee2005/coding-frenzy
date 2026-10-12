"""UVa 11332 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11332-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 2000000000) if rng.random() < 0.7 else rng.randint(1, 100) for _ in range(rng.randint(5, 300))]
if kind == "hidden" and k == 1:
    xs = [1, 9, 10, 18, 19, 2000000000, 1999999999, 999999999]
out("".join(f"{x}\n" for x in xs) + "0\n")
