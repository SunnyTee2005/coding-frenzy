"""UVa 10800 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10800-{kind}-{k}")
out = sys.stdout.write

cases = ["".join(rng.choice("RFC") for _ in range(rng.randint(1, 50))) for _ in range(rng.randint(1, 20))]
if kind == "hidden" and k == 1:
    cases = ["R", "F", "C", "RF", "FR", "R" * 50, "F" * 50, "C" * 50, "RFRFRF", "CCCR"]
out(f"{len(cases)}\n" + "".join(c + "\n" for c in cases))
