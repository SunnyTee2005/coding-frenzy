"""UVa 11364 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11364-{kind}-{k}")
out = sys.stdout.write

cases = [[rng.randint(0, 99) for _ in range(rng.randint(1, 20))] for _ in range(rng.randint(1, 100))]
if kind == "hidden" and k == 1:
    cases = [[0], [99], [0, 99], [5, 5, 5]]
out(f"{len(cases)}\n" + "".join(f"{len(c)}\n{' '.join(map(str, c))}\n" for c in cases))
