"""UVa 1203 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1203-{kind}-{k}")
out = sys.stdout.write

n = rng.randint(1, 30 if k < 10 else 1000)
ids = rng.sample(range(1, 3001), n)
regs = [(q, rng.choice([rng.randint(1, 3000), rng.randint(1, 20)])) for q in ids]
kk = rng.randint(1, 2000 if k > 3 else 50)
if kind == "hidden" and k == 1:
    regs, kk = [(3000, 1), (1, 1)], 6
out("".join(f"Register {q} {p}\n" for q, p in regs) + f"#\n{kk}\n")
