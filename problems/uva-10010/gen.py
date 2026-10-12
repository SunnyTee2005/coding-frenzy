"""UVa 10010 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10010-{kind}-{k}")
out = sys.stdout.write

def case():
    m, n = rng.randint(1, 50 if k >= 8 else 12), rng.randint(1, 50 if k >= 8 else 12)
    alpha = "abAB" if rng.random() < 0.4 else "abcdeABCDE"
    g = ["".join(rng.choice(alpha) for _ in range(n)) for _ in range(m)]
    words = []
    for _ in range(rng.randint(1, 20)):
        i, j = rng.randrange(m), rng.randrange(n)
        dirs = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
        a, b = rng.choice(dirs)
        L, w = rng.randint(1, max(m, n)), ""
        x, y = i, j
        while len(w) < L and 0 <= x < m and 0 <= y < n:
            w += g[x][y]; x += a; y += b
        words.append("".join(c.upper() if rng.random() < 0.5 else c.lower() for c in w))
    return f"{m} {n}\n" + "".join(r + "\n" for r in g) + f"{len(words)}\n" + "".join(w + "\n" for w in words)
T = rng.randint(1, 5)
out(f"{T}\n" + "".join("\n" + case() for _ in range(T)))
