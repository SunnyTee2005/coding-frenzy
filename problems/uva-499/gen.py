"""UVa 499 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"499-{kind}-{k}")
out = sys.stdout.write

# 沒有字母的行要輸出什麼題目沒講，每行至少放一個字母
P = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?-'"
lines = []
for _ in range(rng.randint(1, 120)):
    pool = rng.choice([P, "aAbB .", "xyzXYZ 01"])
    line = "".join(rng.choice(pool) for _ in range(rng.randint(0, 80)))
    lines.append(line + rng.choice("abcXYZ"))
if kind == "hidden" and k == 1:
    lines = ["a", "A", "aA", "Zz zZ", "1a2b3c"]
out("".join(l + "\n" for l in lines))
