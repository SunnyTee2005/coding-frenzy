"""UVa 543 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"543-{kind}-{k}")
out = sys.stdout.write

xs = [2 * rng.randint(3, 499999) for _ in range(rng.randint(5, 300))]
if kind == "hidden" and k == 1:
    xs = [6, 8, 10, 999998, 999996, 128, 98]
out("".join(f"{x}\n" for x in xs) + "0\n")
