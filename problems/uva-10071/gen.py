"""UVa 10071 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10071-{kind}-{k}")
out = sys.stdout.write

qs = [(rng.randint(-100, 100), rng.randint(0, 200)) for _ in range(rng.randint(5, 400))]
if kind == "hidden" and k == 1:
    qs = [(-100, 200), (100, 200), (0, 200), (-1, 0), (1, 1)]
out("".join(f"{v} {t}\n" for v, t in qs))
