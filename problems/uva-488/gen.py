"""UVa 488 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"488-{kind}-{k}")
out = sys.stdout.write

cases = [(rng.randint(1, 9), rng.randint(1, 30)) for _ in range(rng.randint(1, 10))]
if kind == "hidden" and k == 1:
    cases = [(1, 1), (1, 3), (9, 1), (2, 2)]
out(f"{len(cases)}\n\n" + "\n".join(f"{a}\n{f}\n" for a, f in cases))
