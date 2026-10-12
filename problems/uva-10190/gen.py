"""UVa 10190 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10190-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(5, 200)):
    r = rng.random()
    m = rng.choice([2, 3, 5, 7, 10, rng.randint(2, 50), rng.randint(2, 1999999999)])
    if r < 0.5:
        n = 1
        while n * m < 2000000000 and rng.random() < 0.85:
            n *= m
        if n == 1:
            n = m
    else:
        n = rng.randint(2, 1999999999)
    qs.append((n, m))
# 依題意 n=0、m=0、m=1 都得不到合法數列；n=1 是否輸出 "1" 題目沒講清楚，避開
qs += [(rng.randint(2, 1000), 0), (rng.randint(2, 1000), 1), (0, rng.randint(2, 10))] if k % 3 == 0 else []
if kind == "hidden" and k == 1:
    qs = [(2, 2), (1073741824, 2), (1162261467, 3), (1999999999, 1999999999), (4, 3), (0, 0), (5, 1), (0, 5)]
out("".join(f"{n} {m}\n" for n, m in qs))
