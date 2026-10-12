"""UVa 10443 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10443-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 5)):
    r, c = rng.randint(1, 15), rng.randint(1, 15)
    if kind == "hidden" and k == 10 and not cases:
        r, c = 100, 100
    days = rng.randint(0, 20)
    cases.append((r, c, days, ["".join(rng.choice("RSP") for _ in range(c)) for _ in range(r)]))
out(f"{len(cases)}\n" + "".join(f"{r} {c} {d}\n" + "".join(row + "\n" for row in g) for r, c, d, g in cases))
