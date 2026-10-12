"""UVa 913 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"913-{kind}-{k}")
out = sys.stdout.write

xs = [2 * rng.randint(1, 499999999) + 1 for _ in range(rng.randint(3, 100))]
if kind == "hidden" and k == 1:
    xs = [3, 5, 7, 55, 999999999, 999999997]
out("".join(f"{x}\n" for x in xs))
