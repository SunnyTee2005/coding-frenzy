"""UVa 10699 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10699-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 1000000) for _ in range(rng.randint(5, 300))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 3, 4, 6, 30, 210, 2310, 30030, 510510, 999983, 1000000, 65536, 999999]
out("".join(f"{x}\n" for x in xs) + "0\n")
