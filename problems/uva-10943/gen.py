"""UVa 10943 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10943-{kind}-{k}")
out = sys.stdout.write

pairs = [(rng.randint(1, 100), rng.randint(1, 100)) for _ in range(rng.randint(3, 80))]
if kind == "hidden" and k == 1:
    pairs = [(1, 1), (100, 100), (100, 1), (1, 100), (50, 50)]
out("".join(f"{a} {b}\n" for a, b in pairs) + "0 0\n")
