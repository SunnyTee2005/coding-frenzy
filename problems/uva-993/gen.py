"""UVa 993 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"993-{kind}-{k}")
out = sys.stdout.write

def smooth():
    x = 1
    for _ in range(rng.randint(1, 25)):
        f = rng.choice([2, 3, 5, 7])
        if x * f > 10**9: break
        x *= f
    return x
xs = [smooth() if rng.random() < 0.7 else rng.randint(0, 10**9) for _ in range(rng.randint(3, 60))]
if kind == "hidden" and k == 1:
    xs = [0, 1, 2, 9, 10, 11, 12, 36, 49, 100, 1000000000, 999999999, 362880, 13, 7 ** 10]
out(f"{len(xs)}\n" + "".join(f"{x}\n" for x in xs))
