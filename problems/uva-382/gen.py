"""UVa 382 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"382-{kind}-{k}")
out = sys.stdout.write

xs = [rng.randint(1, 60000) for _ in range(rng.randint(2, 98))]
if kind == "hidden" and k == 1:
    xs = [1, 2, 6, 12, 28, 496, 8128, 60000, 59999, 945]
lines, cur = [], []
for x in xs + [0]:
    cur.append(str(x))
    if len(cur) == rng.randint(1, 12) or x == 0:
        lines.append(" ".join(cur)); cur = []
out("\n".join(lines) + "\n")
