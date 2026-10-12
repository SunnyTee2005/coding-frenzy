"""UVa 357 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"357-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(0, 30000) if rng.random() < 0.6 else rng.randint(0, 60) for _ in range(rng.randint(5, 200))]
if kind == "hidden" and k == 1:
    xs = [0, 1, 4, 5, 30000, 29999, 50, 100]
out("".join(f"{x}\n" for x in xs))
