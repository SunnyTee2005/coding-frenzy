"""UVa 11417 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11417-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(2, 500) for _ in range(rng.randint(1, 100))]
if kind == "hidden" and k == 1:
    xs = [2, 3, 500, 499]
out("".join(f"{x}\n" for x in xs) + "0\n")
