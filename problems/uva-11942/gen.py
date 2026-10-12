"""UVa 11942 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11942-{kind}-{k}")
out = sys.stdout.write

def group():
    v = rng.sample(range(1, 100), 10)
    r = rng.random()
    if r < 0.3: v.sort()
    elif r < 0.6: v.sort(reverse=True)
    elif r < 0.75:
        v.sort(); i = rng.randrange(9); v[i], v[i + 1] = v[i + 1], v[i]
    return " ".join(map(str, v))
gs = [group() for _ in range(rng.randint(1, 19))]
out(f"{len(gs)}\n" + "".join(g + "\n" for g in gs))
