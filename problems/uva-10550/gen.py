"""UVa 10550 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10550-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(5, 300)):
    b = rng.randint(0, 39); c = rng.choice([x for x in range(40) if x != b]); d = rng.choice([x for x in range(40) if x != c])
    qs.append((rng.randint(0, 39), b, c, d))
if kind == "hidden" and k == 1:
    qs = [(0, 0, 1, 0), (39, 0, 39, 0), (5, 5, 6, 5), (0, 1, 2, 3), (0, 39, 38, 37)]
out("".join(" ".join(map(str, q)) + "\n" for q in qs) + "0 0 0 0\n")
