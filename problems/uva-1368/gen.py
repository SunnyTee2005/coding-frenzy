"""UVa 1368 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1368-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 4)):
    m, n = rng.randint(4, 30), rng.randint(4, 60)
    if kind == "hidden" and k == 10 and not cases:
        m, n = 20, 1000
    base = "".join(rng.choice("ACGT") for _ in range(n))
    noise = rng.choice([0.1, 0.4, 0.75])
    cases.append(["".join(rng.choice("ACGT") if rng.random() < noise else c for c in base) for _ in range(m)])
if kind == "hidden" and k == 1:
    cases = [["ACGT", "CGTA", "GTAC", "TACG"], ["TTTT", "TTTT", "GGGG", "GGGG"]]
out(f"{len(cases)}\n" + "".join(f"{len(c)} {len(c[0])}\n" + "".join(x + "\n" for x in c) for c in cases))
