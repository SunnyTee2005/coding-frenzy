"""UVa 10041 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10041-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 20)):
    r = rng.randint(1, 499)
    hi = rng.choice([10, 1000, 29999])
    cases.append([rng.randint(1, hi) for _ in range(r)])
if kind == "hidden" and k == 1:
    cases = [[1], [1, 29999], [5, 5, 5], [1, 2, 3, 100]]
out(f"{len(cases)}\n" + "".join(f"{len(c)} {' '.join(map(str, c))}\n" for c in cases))
