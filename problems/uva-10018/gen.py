"""UVa 10018 測資：python3 gen.py <public|hidden> <編號>
只挑「1000 步內得到不超過 4294967295 的迴文」的起始值，符合題目保證。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10018-{kind}-{k}")
LIMIT = 4_294_967_295


def ok(p):
    for _ in range(1000):
        p += int(str(p)[::-1])
        if p > LIMIT:
            return False
        if str(p) == str(p)[::-1]:
            return True
    return False


def pick(lo, hi):
    while True:
        p = rng.randint(lo, hi)
        if ok(p):
            return p


if kind == "hidden" and k == 1:
    # 邊界：一位數、本身就是迴文（仍要加一次）、需要很多步的數
    ps = [1, 9, 11, 121, 4994, 89, 98, 10, 196 + 1, 1000000]
    ps = [p for p in ps if ok(p)]
elif kind == "hidden" and k >= 7:
    ps = [pick(1, 10 ** rng.randint(1, 9)) for _ in range(100)]
else:
    ps = [pick(1, 10 ** rng.randint(1, 6)) for _ in range(rng.randint(3, 30))]
sys.stdout.write(f"{len(ps)}\n" + "".join(f"{p}\n" for p in ps))
