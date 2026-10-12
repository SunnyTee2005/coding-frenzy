"""UVa 442 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"442-{kind}-{k}")
out = sys.stdout.write

names = rng.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", rng.randint(1, 26))
dims = {}
chain = [rng.randint(1, 50) for _ in range(len(names) + 1)]
for i, nm in enumerate(names):
    dims[nm] = (chain[i], chain[i + 1]) if rng.random() < 0.8 else (rng.randint(1, 50), rng.randint(1, 50))
def expr(seq):
    if len(seq) == 1:
        return seq[0]
    cut = rng.randint(1, len(seq) - 1)
    return "(" + expr(seq[:cut]) + expr(seq[cut:]) + ")"
exprs = []
for _ in range(rng.randint(1, 40)):
    if rng.random() < 0.6:
        i = rng.randrange(len(names)); j = rng.randint(i, min(len(names), i + 8) - 1)
        seq = names[i:j + 1]
    else:
        seq = [rng.choice(names) for _ in range(rng.randint(1, 6))]
    exprs.append(expr(seq))
out(f"{len(names)}\n" + "".join(f"{nm} {dims[nm][0]} {dims[nm][1]}\n" for nm in names) + "".join(e + "\n" for e in exprs))
