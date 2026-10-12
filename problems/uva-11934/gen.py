"""UVa 11934 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11934-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(5, 300)):
    qs.append((rng.randint(-1000, 1000), rng.randint(-1000, 1000), rng.randint(-1000, 1000),
               rng.choice([rng.randint(2, 10), rng.randint(2, 999999)]), rng.randint(0, 999)))
if kind == "hidden" and k == 1:
    qs = [(0, 0, 0, 2, 0), (0, 0, 1, 2, 999), (-1000, -1000, -1000, 999999, 999), (1000, 1000, 1000, 2, 999), (0, 0, -6, 3, 5)]
out("".join(" ".join(map(str, q)) + "\n" for q in qs) + "0 0 0 0 0\n")
