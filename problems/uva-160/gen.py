"""UVa 160 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"160-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(2, 100) for _ in range(rng.randint(3, 40))]
if kind == "hidden" and k == 1:
    xs = [2, 3, 47, 48, 53, 100, 99]
if kind == "hidden" and k == 2:
    xs = list(range(2, 101))
out("".join(f"{x}\n" for x in xs) + "0\n")
