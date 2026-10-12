"""UVa 512 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"512-{kind}-{k}")
out = sys.stdout.write

sheets = []
for _ in range(rng.randint(1, 4)):
    r, c = rng.randint(1, 20), rng.randint(1, 20)
    R, C = r, c
    ops = []
    for _ in range(rng.randint(0, 12)):
        kind_ = rng.choice(["EX", "DR", "DC", "IR", "IC", "EX"])
        if kind_ == "EX":
            ops.append(f"EX {rng.randint(1, R)} {rng.randint(1, C)} {rng.randint(1, R)} {rng.randint(1, C)}")
            continue
        size = R if kind_[1] == "R" else C
        if kind_[0] == "D":
            if size <= 1:
                continue
            a = rng.randint(1, min(9, size - 1))
        else:
            a = rng.randint(1, min(9, 50 - size, size)) if size < 50 else 0
            if a == 0:
                continue
        labels = rng.sample(range(1, size + 1), a)
        ops.append(f"{kind_}{' ' * rng.randint(1, 3)}{a} {' '.join(map(str, labels))}")
        delta = -a if kind_[0] == "D" else a
        if kind_[1] == "R":
            R += delta
        else:
            C += delta
    qs = [(rng.randint(1, r), rng.randint(1, c)) for _ in range(rng.randint(1, 20))]
    sheets.append((r, c, ops, qs))
out("".join(f"{r} {c}\n{len(ops)}\n" + "".join(o + "\n" for o in ops) + f"{len(qs)}\n" + "".join(f"{a} {b}\n" for a, b in qs)
            for r, c, ops, qs in sheets) + "0 0\n")
