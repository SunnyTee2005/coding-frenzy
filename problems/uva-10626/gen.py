"""UVa 10626 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10626-{kind}-{k}")
out = sys.stdout.write

cases = []
while len(cases) < rng.randint(1, 8):
    c = rng.randint(1, 150 if k > 5 else 20)
    n1, n5, n10 = rng.randint(0, 500), rng.randint(0, 100), rng.randint(0, 50)
    if n1 + 5 * n5 + 10 * n10 >= 8 * c:  # 題目保證錢夠
        cases.append((c, n1, n5, n10))
if kind == "hidden" and k == 1:
    cases = [(1, 8, 0, 0), (1, 0, 0, 1), (1, 0, 2, 0), (1, 3, 1, 0), (1, 3, 0, 1), (150, 500, 100, 50)]
out(f"{len(cases)}\n" + "".join(" ".join(map(str, x)) + "\n" for x in cases))
