"""UVa 10008 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10008-{kind}-{k}")
out = sys.stdout.write

A = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?'-"
n = rng.randint(1, 60)
lines = ["".join(rng.choice(A if rng.random() < 0.5 else "eEtTaAoO xyz") for _ in range(rng.randint(0, 70))) for _ in range(n)]
if kind == "hidden" and k == 1:
    lines = ["123", "", "!!!", "zZ aA"]
out(f"{len(lines)}\n" + "".join(l + "\n" for l in lines))
