"""UVa 10268 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10268-{kind}-{k}")
out = sys.stdout.write

LIM = 2**31
cases = []
while len(cases) < rng.randint(3, 150):
    x = rng.randint(-10, 10) if rng.random() < 0.8 else rng.randint(-1000, 1000)
    deg = rng.randint(0, 8)
    a = [rng.randint(-100, 100) for _ in range(deg + 1)]
    n, r, ok = deg, 0, True
    for i in range(n):  # 確保 Horner 每一步都在 int 範圍內
        r = r * x + a[i] * (n - i)
        ok &= abs(r) < LIM and abs(r * x) < LIM
    if ok:
        cases.append((x, a))
if kind == "hidden" and k == 1:
    cases = [(0, [5]), (0, [1, 2, 3]), (-1, [1, 1, 1, 1]), (100000, [0, 1, 0])]
out("".join(f"{x}\n{' '.join(map(str, a))}\n" for x, a in cases))
