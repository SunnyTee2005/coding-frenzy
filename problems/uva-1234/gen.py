"""UVa 1234 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1234-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 5)):
    n = rng.randint(1, 60 if k < 10 else 400)
    edges = []
    for v in range(2, n + 1):  # 先連成一棵樹，保證連通
        edges.append((rng.randint(1, v - 1), v, rng.randint(1, 1000)))
    for _ in range(rng.randint(0, 2 * n if n > 1 else 0)):
        a, b = rng.sample(range(1, n + 1), 2)
        edges.append((a, b, rng.choice([rng.randint(1, 1000), rng.randint(1, 5)])))
    if not edges:
        continue
    rng.shuffle(edges)
    cases.append((n, edges))
if not cases:
    cases = [(2, [(1, 2, 7)])]
if kind == "hidden" and k == 1:
    cases = [(2, [(1, 2, 7)]), (2, [(1, 2, 7), (2, 1, 3)]), (3, [(1, 2, 1), (2, 3, 1), (3, 1, 1)])]
out(f"{len(cases)}\n" + "".join(f"{n} {len(e)}\n" + "".join(f"{a} {b} {c}\n" for a, b, c in e) for n, e in cases) + "0\n")
