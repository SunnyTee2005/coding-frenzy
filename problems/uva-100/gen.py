"""UVa 100 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"100-{kind}-{k}")
out = sys.stdout.write

pairs = []
for _ in range(rng.randint(3, 30)):
    a = rng.randint(1, 999999); b = min(999999, max(1, a + rng.randint(-3000, 3000)))
    pairs.append((a, b))
if kind == "hidden" and k == 1:
    pairs = [(1, 1), (10, 1), (999999, 999999), (837799, 837799), (1, 2)]
out("".join(f"{a} {b}\n" for a, b in pairs))
