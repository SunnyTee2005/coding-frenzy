"""UVa 10161 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10161-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 2 * 10**9) for _ in range(rng.randint(3, 100))]
if kind == "hidden" and k == 1:
    xs = list(range(1, 30)) + [2 * 10**9, 44721 ** 2, 44721 ** 2 + 1]
out("".join(f"{x}\n" for x in xs) + "0\n")
