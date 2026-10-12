"""UVa 11526 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11526-{kind}-{k}")
out = sys.stdout.write

xs = [rng.choice([rng.randint(1, 2**31 - 1), rng.randint(1, 1000), rng.randint(-2**31, 0)]) for _ in range(rng.randint(1, 300))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 0, -1, -2147483648, 2147483647, 1000000]
out(f"{len(xs)}\n" + "".join(f"{x}\n" for x in xs))
