"""UVa 907 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"907-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 8)):
    n = rng.randint(1, 40 if k < 10 else 150)
    kk = rng.randint(0, min(n, 300))
    hi = rng.choice([5, 100, 10000])
    cases.append((n, kk, [rng.randint(1, hi) for _ in range(n + 1)]))
if kind == "hidden" and k == 1:
    cases = [(1, 0, [3, 4]), (1, 1, [3, 4]), (3, 3, [1, 1, 1, 9])]
out("".join(f"{n} {kk}\n" + "".join(f"{x}\n" for x in d) for n, kk, d in cases))
