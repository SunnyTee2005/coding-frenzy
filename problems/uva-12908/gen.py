"""UVa 12908 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12908-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 10**8) if rng.random() < 0.6 else rng.randint(1, 100) for _ in range(rng.randint(5, 300))]
if kind == "hidden" and k == 1:
    xs = [1, 10**8, 99999999, 14141 * 14142 // 2, 14141 * 14142 // 2 - 1, 10, 15]
out("".join(f"{x}\n" for x in xs) + "0\n")
