"""UVa 11678 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11678-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 10)):
    hi = rng.choice([10, 100, 100000])
    a = sorted(rng.randint(1, hi) for _ in range(rng.randint(1, 300)))
    b = sorted(rng.randint(1, hi) for _ in range(rng.randint(1, 300)))
    cases.append((a, b))
if kind == "hidden" and k == 10:
    cases = [(sorted(rng.randint(1, 100000) for _ in range(2000)), sorted(rng.randint(1, 100000) for _ in range(2000)))]
if kind == "hidden" and k == 1:
    cases = [([1], [2]), ([1, 1, 1], [1]), ([1, 2, 3], [4, 4, 4]), ([100000], [1])]
out("".join(f"{len(a)} {len(b)}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}\n" for a, b in cases) + "0 0\n")
