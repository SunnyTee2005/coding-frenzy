"""UVa 496 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"496-{kind}-{k}")
out = sys.stdout.write

def pair():
    base = rng.sample(range(1, 60), rng.randint(1, 12))
    r = rng.random()
    if r < 0.2: a, b = base, rng.sample(base, len(base))
    elif r < 0.4: a, b = base, base + rng.sample([x for x in range(60, 99)], rng.randint(1, 4))
    elif r < 0.6: a, b = base + rng.sample([x for x in range(60, 99)], rng.randint(1, 4)), base
    elif r < 0.8: a, b = base, rng.sample(range(100, 160), rng.randint(1, 8))
    else: a, b = base + [200], base[:1] + [300]
    return " ".join(map(str, a)) + "\n" + " ".join(map(str, b)) + "\n"
out("".join(pair() for _ in range(rng.randint(3, 60))))
