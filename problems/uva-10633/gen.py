"""UVa 10633 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10633-{kind}-{k}")
out = sys.stdout.write

xs = []
for _ in range(rng.randint(5, 300)):
    x = rng.choice([rng.randint(10, 10**18), rng.randint(10, 200)])
    if rng.random() < 0.3:
        x -= x % 9  # 9 的倍數有兩個答案
        x = max(x, 18)
    xs.append(x)
if kind == "hidden" and k == 1:
    xs = [10, 17, 18, 19, 27, 10**18, 999999999999999999, 10**18 - 1]
out("".join(f"{x}\n" for x in xs) + "0\n")
