"""UVa 11000 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11000-{kind}-{k}")
out = sys.stdout.write

# 題目保證兩數不超過 2^32，N 最多到 45
xs = [rng.randint(0, 45) for _ in range(rng.randint(3, 100))]
if kind == "hidden" and k == 1:
    xs = [0, 1, 2, 45, 44]
out("".join(f"{x}\n" for x in xs) + "-1\n")
