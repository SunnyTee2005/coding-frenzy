"""UVa 834 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"834-{kind}-{k}")
out = sys.stdout.write

from math import gcd
qs = []
while len(qs) < rng.randint(5, 200):
    hi = rng.choice([20, 1000, 1000000])
    a, b = rng.randint(1, hi), rng.randint(2, hi)
    if a % b:  # 題目沒有說明整數的輸出格式，避開
        qs.append((a, b))
if kind == "hidden" and k == 1:
    qs = [(1, 2), (2, 3), (3, 2), (1, 1000000), (999999, 1000000), (1000000, 999999), (6, 4)]
out("".join(f"{a} {b}\n" for a, b in qs))
