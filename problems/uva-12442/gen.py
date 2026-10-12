"""UVa 12442 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12442-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 6 if k < 10 else 1)):
    n = rng.randint(2, 60 if k < 10 else 5000)
    nxt = {}
    for u in range(1, n + 1):
        v = rng.randint(1, n - 1)
        nxt[u] = v + (v >= u)
    lines = [(u, nxt[u]) for u in range(1, n + 1)]
    rng.shuffle(lines)
    cases.append(lines)
if kind == "hidden" and k == 1:
    cases = [[(1, 2), (2, 1)], [(2, 1), (1, 2)], [(1, 2), (2, 3), (3, 2)]]
out(f"{len(cases)}\n" + "".join(f"{len(c)}\n" + "".join(f"{u} {v}\n" for u, v in c) for c in cases))
