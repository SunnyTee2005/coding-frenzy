"""UVa 13178 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"13178-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 2**31 - 1) for _ in range(rng.randint(3, 100))]
if kind == "hidden" and k == 1:
    xs = list(range(1, 20)) + [2**31 - 1, 2**31 - 2, 2**31 - 3]
out(f"{len(xs)}\n" + "".join(f"{x}\n" for x in xs))
