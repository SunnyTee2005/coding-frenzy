"""UVa 11220 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11220-{kind}-{k}")
out = sys.stdout.write

def word():
    return "".join(rng.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(rng.randint(1, rng.choice([3, 8, 30]))))
cases = []
for _ in range(rng.randint(1, 15 if k > 5 else 5)):
    lines = []
    for _ in range(rng.randint(1, 12)):
        ws = [word() for _ in range(rng.randint(1, 30))]
        lines.append("".join(w + " " * rng.choice([1, 1, 1, 2, 3]) for w in ws).rstrip())
    cases.append(lines)
out(f"{len(cases)}\n\n" + "".join("".join(l + "\n" for l in c) + "\n" for c in cases))
