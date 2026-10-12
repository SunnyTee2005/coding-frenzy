"""UVa 13204 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"13204-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 1000000) if rng.random() < 0.6 else rng.randint(1, 12) for _ in range(rng.randint(5, 300))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 3, 4, 5, 999999, 1000000]
out("".join(f"{x}\n" for x in xs))
