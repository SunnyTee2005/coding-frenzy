"""UVa 10050 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10050-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 15)):
    n = rng.randint(7, 3650)
    hs = []
    while len(hs) < rng.randint(1, 100 if k == 10 else 8):
        h = rng.choice([rng.randint(1, 20), rng.randint(1, 3650)])
        if h % 7:
            hs.append(h)
    cases.append((n, hs))
if kind == "hidden" and k == 1:
    cases = [(7, [1]), (3650, [1]), (7, [6]), (14, [13]), (3650, [3649])]
out(f"{len(cases)}\n" + "".join(f"{n}\n{len(hs)}\n" + "".join(f"{h}\n" for h in hs) for n, hs in cases))
