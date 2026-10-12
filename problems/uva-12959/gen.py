"""UVa 12959 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12959-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 15)):
    j, r = rng.randint(1, 20), rng.randint(1, 20)
    if kind == "hidden" and k == 10 and not cases:
        j, r = 100, 50
    hi = rng.choice([1, 2, 100])
    cases.append((j, r, [rng.randint(0, hi) for _ in range(j * r)]))
if kind == "hidden" and k == 1:
    cases = [(1, 1, [0]), (2, 1, [5, 5]), (3, 2, [0, 0, 0, 0, 0, 0]), (2, 2, [100, 0, 0, 99])]
out("".join(f"{j} {r}\n{' '.join(map(str, v))}\n" for j, r, v in cases) + "0 0\n")
