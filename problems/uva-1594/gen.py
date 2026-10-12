"""UVa 1594 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1594-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 60)):
    n = rng.choice([4, 8, rng.randint(3, 15)])
    hi = rng.choice([1, 3, 1000])
    cases.append([rng.randint(0, hi) for _ in range(n)])
if kind == "hidden" and k == 1:
    cases = [[0, 0, 0], [1, 1, 1], [1, 0, 0], [1000] * 15, [1, 0] * 4, [0, 1000, 0, 1000, 0, 1000, 0, 1000]]
out(f"{len(cases)}\n" + "".join(f"{len(c)}\n{' '.join(map(str, c))}\n" for c in cases))
