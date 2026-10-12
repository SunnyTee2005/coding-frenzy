"""UVa 10696 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10696-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 1000000) if rng.random() < 0.4 else rng.randint(1, 200) for _ in range(rng.randint(3, 300))]
if kind == "hidden" and k == 1:
    xs = [1, 90, 91, 100, 101, 102, 1000000]
out("".join(f"{x}\n" for x in xs) + "0\n")
