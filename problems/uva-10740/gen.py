"""UVa 10740 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10740-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 8)):
    n = rng.randint(2, 12 if k < 10 else 100)
    m = rng.randint(1, min(1000, 3 * n if k < 10 else 600))
    x, y = rng.sample(range(1, n + 1), 2)
    edges = [(rng.randint(1, n), rng.randint(1, n), rng.choice([0, rng.randint(0, 10), rng.randint(0, 10000)])) for _ in range(m)]
    # 題目保證 x 到 y 至少有一條路
    path = [x] + rng.sample([v for v in range(1, n + 1) if v not in (x, y)], rng.randint(0, min(3, n - 2))) + [y]
    edges += [(a, b, rng.randint(0, 100)) for a, b in zip(path, path[1:])]
    rng.shuffle(edges)
    cases.append((n, x, y, rng.randint(2, 10), edges))
if kind == "hidden" and k == 1:
    cases = [(2, 1, 2, 2, [(1, 2, 0)]), (2, 1, 2, 10, [(1, 2, 0), (2, 1, 0)]), (2, 2, 1, 3, [(2, 1, 7), (1, 1, 0)])]
out("".join(f"{n} {len(e)}\n{x} {y} {kk}\n" + "".join(f"{u} {v} {l}\n" for u, v, l in e) for n, x, y, kk, e in cases) + "0 0\n")
