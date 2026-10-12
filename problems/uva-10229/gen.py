"""UVa 10229 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10229-{kind}-{k}")
out = sys.stdout.write

qs = [(rng.choice([rng.randint(0, 2147483647), rng.randint(0, 50)]), rng.randint(0, 20)) for _ in range(rng.randint(5, 300))]
if kind == "hidden" and k == 1:
    qs = [(0, 0), (0, 20), (1, 0), (1, 1), (2147483647, 20), (2, 20), (30, 20)]
out("".join(f"{n} {m}\n" for n, m in qs))
