"""UVa 11764 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11764-{kind}-{k}")
out = sys.stdout.write

cases = [[rng.randint(1, 10) for _ in range(rng.randint(1, 49))] for _ in range(rng.randint(1, 29))]
if kind == "hidden" and k == 1:
    cases = [[1], [10, 10], [1, 10], [10, 1]]
out(f"{len(cases)}\n" + "".join(f"{len(c)}\n{' '.join(map(str, c))}\n" for c in cases))
