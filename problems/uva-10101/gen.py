"""UVa 10101 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10101-{kind}-{k}")
out = sys.stdout.write

# 輸入 0 時要印什麼題目沒講，避開
xs = []
for _ in range(rng.randint(3, 200)):
    d = rng.randint(1, 15)
    x = rng.randint(10 ** (d - 1), 10 ** d - 1)
    if rng.random() < 0.3:  # 製造中間有零的數字
        s = list(str(x))
        for i in range(1, len(s)):
            if rng.random() < 0.5:
                s[i] = "0"
        x = int("".join(s))
    xs.append(x)
if kind == "hidden" and k == 1:
    xs = [1, 100, 1000, 100000, 10000000, 100000000000000, 999999999999999, 10000000000000, 100000000000]
out("".join(f"{x}\n" for x in xs))
