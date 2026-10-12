"""UVa 1583 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1583-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 100000) if rng.random() < 0.7 else rng.randint(1, 200) for _ in range(rng.randint(1, 500))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 3, 100000, 99999, 101, 198, 216]
out(f"{len(xs)}\n" + "".join(f"{x}\n" for x in xs))
