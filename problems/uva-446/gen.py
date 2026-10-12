"""UVa 446 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"446-{kind}-{k}")
out = sys.stdout.write

lines = []
for _ in range(rng.randint(3, 60)):
    a, b = rng.randint(0, 0xFFF), rng.randint(0, 0xFFF)
    lines.append(f"{a:X} {rng.choice('+-')} {b:X}")
if kind == "hidden" and k == 1:
    lines = ["0 + 0", "FFF + FFF", "0 - FFF", "FFF - 0", "1 - 2"]
out(f"{len(lines)}\n" + "".join(l + "\n" for l in lines))
