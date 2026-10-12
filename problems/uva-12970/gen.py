"""UVa 12970 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12970-{kind}-{k}")
out = sys.stdout.write

qs = []
while len(qs) < rng.randint(3, 200):
    hi = rng.choice([10, 1000, 10**9])
    v1, d1, v2, d2 = (rng.randint(1, hi) for _ in range(4))
    if d1 * v2 != d2 * v1:
        qs.append((v1, d1, v2, d2))
if kind == "hidden" and k == 1:
    qs = [(1, 1, 1, 2), (10**9, 10**9, 1, 10**9), (1, 10**9, 10**9, 1), (10**9, 1, 10**9 - 1, 1), (3, 6, 2, 2)]
out("".join(" ".join(map(str, q)) + "\n" for q in qs) + "0 0 0 0\n")
