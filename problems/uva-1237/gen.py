"""UVa 1237 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1237-{kind}-{k}")
out = sys.stdout.write

def name():
    return "".join(rng.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ-_0123456789") for _ in range(rng.randint(1, 20)))
cases = []
for _ in range(rng.randint(1, 4)):
    hi = rng.choice([100, 1000000])
    db = []
    for _ in range(rng.randint(1, 60)):
        l = rng.randint(1, hi - 2); h = rng.randint(l + 1, min(hi - 1, l + rng.choice([5, 50, hi])))
        db.append((name(), l, h))
    qs = [rng.choice([rng.randint(1, hi - 1), rng.choice(db)[1], rng.choice(db)[2]]) for _ in range(rng.randint(1, 120))]
    cases.append((db, qs))
if kind == "hidden" and k == 1:
    cases = [([("A", 1, 2)], [1, 2, 3]), ([("A", 1, 5), ("B", 5, 9)], [4, 5, 6, 10])]
out(f"{len(cases)}\n" + "".join(f"{len(db)}\n" + "".join(f"{n} {l} {h}\n" for n, l, h in db) + f"{len(qs)}\n" + "".join(f"{p}\n" for p in qs)
                             for db, qs in cases))
