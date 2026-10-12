"""UVa 11461 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11461-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(5, 200)):
    a = rng.randint(1, 100000); b = rng.randint(a, min(100000, a + rng.choice([0, 10, 1000, 100000])))
    qs.append((a, b))
if kind == "hidden" and k == 1:
    qs = [(1, 1), (2, 3), (4, 4), (1, 100000), (99999, 100000), (100000, 100000), (99856, 99856)]
out("".join(f"{a} {b}\n" for a, b in qs) + "0 0\n")
