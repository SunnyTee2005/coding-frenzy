"""UVa 11321 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11321-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 6)):
    n, m = rng.randint(1, 300), rng.choice([1, 2, 3, 7, rng.randint(1, 10000)])
    hi = rng.choice([20, 2**31 - 1])
    cases.append((m, [rng.randint(-hi - 1 if hi > 20 else -hi, hi) for _ in range(n)]))
if kind == "hidden" and k == 1:
    cases = [(1, [5, -5, 0, 2, -2]), (10000, [-2147483648, 2147483647, 0, -1, 1]), (4, [-100, -4, 4, 100, -3, 3])]
out("".join(f"{len(v)} {m}\n" + "".join(f"{x}\n" for x in v) for m, v in cases) + "0 0\n")
