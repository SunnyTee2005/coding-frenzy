"""UVa 11192 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11192-{kind}-{k}")
out = sys.stdout.write

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
qs = []
for _ in range(rng.randint(1, 100)):
    g = rng.randint(1, 9)
    length = g * rng.randint(1, 100 // g)
    qs.append((g, "".join(rng.choice(A) for _ in range(length))))
if kind == "hidden" and k == 1:
    qs = [(1, "A"), (1, "AB"), (2, "AB"), (9, "123456789"), (4, "x" * 100)]
out("".join(f"{g} {s}\n" for g, s in qs) + "0\n")
