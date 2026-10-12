"""UVa 482 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"482-{kind}-{k}")
out = sys.stdout.write

def num():
    r = rng.random()
    if r < 0.3:
        return str(rng.randint(-1000, 1000))
    if r < 0.8:
        return f"{rng.uniform(-1000, 1000):.{rng.randint(1, 4)}f}"
    return rng.choice(["0.0", "-0.5", "1e3", "3.14159", ".5", "-2"])
cases = []
for _ in range(rng.randint(1, 10)):
    n = rng.randint(1, 60)
    p = list(range(1, n + 1)); rng.shuffle(p)
    cases.append((p, [num() for _ in range(n)]))
if kind == "hidden" and k == 1:
    cases = [([1], ["7"]), ([2, 1], ["1.50", "-0.25"])]
out(f"{len(cases)}\n\n" + "\n".join(f"{' '.join(map(str, p))}\n{' '.join(v)}\n" for p, v in cases))
