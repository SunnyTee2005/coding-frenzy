"""UVa 10931 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10931-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 2147483647) if rng.random() < 0.6 else rng.randint(1, 1000) for _ in range(rng.randint(5, 150))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 3, 2147483647, 1073741824, 255, 256]
out("".join(f"{x}\n" for x in xs) + "0\n")
