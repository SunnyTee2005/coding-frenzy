"""UVa 12650 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12650-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 30)):
    n = rng.randint(1, 10000 if (kind == "hidden" and k == 10 and not cases) else 100)
    r = rng.choice([n, rng.randint(1, n)])
    ids = rng.sample(range(1, n + 1), r)
    cases.append((n, ids))
if kind == "hidden" and k == 1:
    cases = [(1, [1]), (2, [2]), (2, [1]), (3, [2])]
out("".join(f"{n} {len(ids)}\n{' '.join(map(str, ids))}\n" for n, ids in cases))
