"""UVa 665 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"665-{kind}-{k}")
out = sys.stdout.write

sets = []
for _ in range(rng.randint(1, 6)):
    n = rng.randint(2, 100 if k > 5 else 12)
    false, delta = rng.randint(1, n), rng.choice([-1, 1])
    ws = []
    for _ in range(rng.randint(1, min(100, 3 * n))):
        p = rng.randint(1, n // 2)
        coins = rng.sample(range(1, n + 1), 2 * p)
        left, right = coins[:p], coins[p:]
        if rng.random() < 0.3 and false not in coins and n >= 2:
            pass
        w = (delta if false in left else 0) - (delta if false in right else 0)
        ws.append((left, right, "=" if w == 0 else (">" if w > 0 else "<")))
    sets.append((n, ws))
out(f"{len(sets)}\n\n" + "\n".join(f"{n} {len(ws)}\n" + "".join(f"{len(l)} {' '.join(map(str, l))} {' '.join(map(str, r))}\n{res}\n" for l, r, res in ws)
                                 for n, ws in sets))
