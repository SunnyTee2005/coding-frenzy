"""UVa 299 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"299-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 60)):
    l = rng.randint(1, 50)
    p = list(range(1, l + 1)); rng.shuffle(p)
    cases.append(p)
if kind == "hidden" and k == 1:
    cases = [[], [1], list(range(50, 0, -1)), list(range(1, 51))]
out(f"{len(cases)}\n" + "".join(f"{len(p)}\n{' '.join(map(str, p))}\n" for p in cases))
