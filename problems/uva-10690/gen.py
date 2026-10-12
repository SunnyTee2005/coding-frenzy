"""UVa 10690 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10690-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 15 if k < 10 else 40)):
    n, m = rng.randint(1, 50), rng.randint(1, 50)
    if k < 4:
        n, m = rng.randint(1, 5), rng.randint(1, 5)
    hi = rng.choice([3, 50])
    cases.append((n, m, [rng.randint(-hi, hi) for _ in range(n + m)]))
if kind == "hidden" and k == 1:
    cases = [(1, 1, [-50, 50]), (1, 1, [0, 0]), (50, 50, [50] * 100), (50, 50, [-50] * 100), (1, 2, [-1, -2, 3])]
out("".join(f"{n} {m}\n{' '.join(map(str, a))}\n" for n, m, a in cases))
