"""UVa 12019 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12019-{kind}-{k}")
out = sys.stdout.write

DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
qs = []
for _ in range(rng.randint(1, 365)):
    m = rng.randint(1, 12)
    qs.append((m, rng.randint(1, DAYS[m - 1])))
if kind == "hidden" and k == 1:
    qs = [(1, 1), (12, 31), (2, 28), (3, 1), (4, 4), (6, 6), (7, 11), (11, 7)]
out(f"{len(qs)}\n" + "".join(f"{m} {d}\n" for m, d in qs))
