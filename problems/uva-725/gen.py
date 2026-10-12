"""UVa 725 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"725-{kind}-{k}")
out = sys.stdout.write

ns = rng.sample(range(2, 80), rng.randint(1, 12))
if kind == "hidden" and k == 1:
    ns = [2, 79, 3]
if kind == "hidden" and k == 2:
    ns = list(range(2, 80))
out("".join(f"{n}\n" for n in ns) + "0\n")
