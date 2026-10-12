"""UVa 441 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"441-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(1 if kind == "hidden" and k == 10 else rng.randint(1, 3)):
    kk = 12 if kind == "hidden" and k == 10 else rng.randint(7, 9)
    cases.append(sorted(rng.sample(range(1, 50), kk)))
if kind == "hidden" and k == 1:
    cases = [[1, 2, 3, 4, 5, 6, 7], [40, 41, 42, 43, 44, 45, 46, 47, 48]]
out("".join(f"{len(c)} {' '.join(map(str, c))}\n" for c in cases) + "0\n")
