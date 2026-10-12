"""UVa 706 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"706-{kind}-{k}")
out = sys.stdout.write

cases = [(rng.randint(1, 4 if k < 9 else 10), rng.randint(0, 10 ** rng.randint(1, 8) - 1)) for _ in range(rng.randint(1, 6))]
if kind == "hidden" and k == 1:
    cases = [(1, 0), (1, 1234567890 % 99999999), (2, 88888888), (1, 7), (10, 0)]
out("".join(f"{s} {n}\n" for s, n in cases) + "0 0\n")
