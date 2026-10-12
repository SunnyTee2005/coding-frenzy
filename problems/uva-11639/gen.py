"""UVa 11639 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11639-{kind}-{k}")
out = sys.stdout.write

def rect():
    x1, x2 = sorted(rng.sample(range(0, 101), 2)); y1, y2 = sorted(rng.sample(range(0, 101), 2))
    return f"{x1} {y1} {x2} {y2}"
nights = [(rect(), rect()) for _ in range(rng.randint(1, 100))]
if kind == "hidden" and k == 1:
    nights = [("0 0 100 100", "0 0 100 100"), ("0 0 50 50", "50 50 100 100"), ("0 0 1 1", "99 99 100 100"), ("10 10 90 90", "20 20 30 30")]
out(f"{len(nights)}\n" + "".join(f"{a}\n{b}\n" for a, b in nights))
