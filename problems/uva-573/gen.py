"""UVa 573 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"573-{kind}-{k}")
out = sys.stdout.write

qs = [(rng.randint(1, 100), rng.randint(1, 100), rng.randint(1, 100), rng.randint(1, 100)) for _ in range(rng.randint(5, 300))]
if kind == "hidden" and k == 1:
    qs = [(1, 1, 1, 1), (100, 100, 100, 100), (100, 1, 1, 1), (100, 100, 1, 1), (1, 100, 100, 100)]
out("".join(" ".join(map(str, q)) + "\n" for q in qs) + "0 0 0 0\n")
