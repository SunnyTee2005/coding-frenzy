"""UVa 13242 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"13242-{kind}-{k}")
out = sys.stdout.write

from fractions import Fraction
def best(cap, target, jars):
    cand = []
    for i in range(len(jars)):
        vol = heat = 0
        for j in range(i, len(jars)):
            vol += jars[j][0]; heat += jars[j][0] * jars[j][1]
            if vol > cap:
                break
            if 2 * vol >= cap:
                d = abs(Fraction(heat, vol) - target)
                if d <= 5:
                    cand.append(d)
    cand.sort()
    return cand
cases = []
while len(cases) < rng.randint(1, 6):
    n = rng.randint(1, 60 if k < 10 else 400)
    jars = [(rng.randint(1, 100), rng.randint(0, 100)) for _ in range(n)]
    total = sum(v for v, _ in jars)
    cap = rng.randint(1, max(1, total // rng.choice([1, 3, 10])))
    target = rng.randint(0, 100) if rng.random() < 0.3 else jars[rng.randrange(n)][1]
    c = best(cap, target, jars)
    # 題目沒講平手（溫差完全相同）時怎麼選以外的細節；為了保險，不出最佳溫差平手的資料
    if len(c) >= 2 and c[0] == c[1]:
        continue
    cases.append((cap, target, jars))
out(f"{len(cases)}\n" + "".join(f"{cap} {t}\n{len(j)}\n" + "".join(f"{v} {tp}\n" for v, tp in j) for cap, t, j in cases))
