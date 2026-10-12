"""UVa 11728 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11728-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 1000) for _ in range(rng.randint(5, 200))]
if kind == "hidden" and k == 1:
    xs = list(range(1, 60)) + [1000, 999, 998]
out("".join(f"{x}\n" for x in xs) + "0\n")
