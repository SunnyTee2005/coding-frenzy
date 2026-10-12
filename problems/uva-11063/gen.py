"""UVa 11063 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11063-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(3, 20)):
    n = rng.randint(2, 100)
    mode = rng.random()
    if mode < 0.4:  # 貪心建出真正的 B2 序列
        b, sums, x = [], set(), rng.randint(1, 5)
        while len(b) < n and x <= 10000:
            new = {x + y for y in b} | {2 * x}
            if not (new & sums):
                sums |= new; b.append(x)
            x += rng.randint(1, 3)
        if len(b) < 2:
            b = [1, 2]
    elif mode < 0.7:
        b = sorted(rng.sample(range(1, 10001), n))
    else:
        b = [rng.randint(1, 10000) for _ in range(n)]
        if rng.random() < 0.3:
            b = sorted(b)
    cases.append(b)
if kind == "hidden" and k == 1:
    cases = [[1, 2], [2, 1], [1, 1], [1, 2, 3], [1, 2, 4, 8, 16], [9999, 10000], [5, 6, 8]]
out("".join(f"{len(b)}\n{' '.join(map(str, b))}\n\n" for b in cases))
