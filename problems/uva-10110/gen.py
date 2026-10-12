"""UVa 10110 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10110-{kind}-{k}")
out = sys.stdout.write

xs = []
for _ in range(rng.randint(5, 300)):
    if rng.random() < 0.4:
        r = rng.randint(1, 65535); xs.append(r * r + rng.choice([0, 0, -1, 1]))
    else:
        xs.append(rng.randint(1, 2**32 - 2))
xs = [x for x in xs if 1 <= x <= 2**32 - 2]
if kind == "hidden" and k == 1:
    xs = [1, 2, 3, 4, 65535 * 65535, 65535 * 65535 - 1, 2**32 - 2, 4294836225]
out("".join(f"{x}\n" for x in xs) + "0\n")
