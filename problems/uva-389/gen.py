"""UVa 389 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"389-{kind}-{k}")
out = sys.stdout.write

D = "0123456789ABCDEF"
lines = []
for _ in range(rng.randint(5, 200)):
    a, b = rng.randint(2, 16), rng.randint(2, 16)
    num = "".join(rng.choice(D[:a]) for _ in range(rng.randint(1, 7)))
    if rng.random() < 0.2:
        num = "0" * rng.randint(1, 3) + num[:4]
    sp = lambda: " " * rng.choice([1, 1, 1, 2, 3])
    lines.append(" " * rng.choice([0, 0, 2, 5]) + num + sp() + str(a) + sp() + str(b) + " " * rng.choice([0, 0, 1]))
if kind == "hidden" and k == 1:
    lines = ["0 2 10", "0000000 16 2", "FFFFFFF 16 2", "FFFFFFF 16 16", "1111111 2 2", "9999999 10 16", "10000000 2 10"]
out("".join(l + "\n" for l in lines))
