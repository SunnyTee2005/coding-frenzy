"""UVa 11956 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11956-{kind}-{k}")
out = sys.stdout.write

progs = ["".join(rng.choice("+++--><<>.") for _ in range(rng.randint(1, 100000 if k == 10 else 300))) for _ in range(rng.randint(1, 5 if k != 10 else 1))]
if kind == "hidden" and k == 1:
    progs = ["<+", ">" * 100 + "+", "-", "+" * 256, "." * 10]
out(f"{len(progs)}\n" + "".join(p + "\n" for p in progs))
