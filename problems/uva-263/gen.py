"""UVa 263 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"263-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 999999999) if rng.random() < 0.5 else rng.randint(1, 9999) for _ in range(rng.randint(3, 40))]
if kind == "hidden" and k == 1:
    xs = [1, 9, 10, 100, 999999999, 6174, 495, 111111111]
out("".join(f"{x}\n" for x in xs) + "0\n")
