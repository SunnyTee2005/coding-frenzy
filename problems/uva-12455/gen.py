"""UVa 12455 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12455-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 15 if k < 10 else 50)):
    p = rng.randint(1, 20)
    bars = [rng.randint(1, rng.choice([10, 100, 1000])) for _ in range(p)]
    if rng.random() < 0.5:
        n = sum(x for x in bars if rng.random() < 0.3)
        n = min(n, 1000)
    else:
        n = rng.randint(0, 1000)
    cases.append((n, bars))
if kind == "hidden" and k == 1:
    cases = [(0, [5]), (5, [5]), (1000, [1000]), (999, [1000]), (1000, [50] * 20), (1, [2] * 20)]
out(f"{len(cases)}\n" + "".join(f"{n}\n{len(b)}\n{' '.join(map(str, b))}\n" for n, b in cases))
