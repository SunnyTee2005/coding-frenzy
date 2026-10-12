"""UVa 12468 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12468-{kind}-{k}")
out = sys.stdout.write

pairs = [(rng.randint(0, 99), rng.randint(0, 99)) for _ in range(rng.randint(3, 200))]
if kind == "hidden" and k == 1:
    pairs = [(0, 0), (0, 99), (99, 0), (0, 50), (50, 0), (0, 51), (25, 75), (1, 98)]
out("".join(f"{a} {b}\n" for a, b in pairs) + "-1 -1\n")
