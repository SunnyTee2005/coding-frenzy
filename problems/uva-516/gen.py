"""UVa 516 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"516-{kind}-{k}")
out = sys.stdout.write

def factor(x):
    f, d = [], 2
    while d * d <= x:
        c = 0
        while x % d == 0:
            x //= d; c += 1
        if c: f.append((d, c))
        d += 1
    if x > 1: f.append((x, 1))
    return f
xs = [rng.randint(3, 32767) for _ in range(rng.randint(3, 200))]
if kind == "hidden" and k == 1:
    xs = [3, 4, 32767, 32768 - 1, 2 ** 15 - 1, 16384, 30031, 3 * 5 * 7 * 11 * 13]
xs = [x for x in xs if 2 < x <= 32767]
out("".join(" ".join(f"{p} {e}" for p, e in reversed(factor(x))) + "\n" for x in xs) + "0\n")
