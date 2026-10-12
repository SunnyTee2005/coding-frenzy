"""UVa 10858 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10858-{kind}-{k}")
out = sys.stdout.write

SMOOTH = [2, 3, 5, 7]
xs = []
for _ in range(rng.randint(3, 12)):
    if rng.random() < 0.5:
        x = 1
        for _ in range(rng.randint(1, 6)):
            x *= rng.choice(SMOOTH)
        xs.append(x)
    else:
        xs.append(rng.choice([rng.randint(2, 200), rng.randint(2, 2000000000)]))
if kind == "hidden" and k == 1:
    xs = [1, 2, 4, 1999999973, 1999999998, 64]
out("".join(f"{x}\n" for x in xs) + "0\n")
