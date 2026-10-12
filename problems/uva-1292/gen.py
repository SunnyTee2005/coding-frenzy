"""UVa 1292 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1292-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 5)):
    n = rng.randint(1, 15 if k < 6 else (1500 if k == 10 else 200))
    label = list(range(n)); rng.shuffle(label)
    children = {i: [] for i in range(n)}
    for i in range(1, n):
        children[rng.randint(max(0, i - rng.choice([1, 3, i])), i - 1)].append(i)
    lines = [f"{label[i]}:({len(children[i])})" + "".join(f" {label[c]}" for c in children[i]) for i in range(n)]
    rng.shuffle(lines)
    cases.append(lines)
out("".join(f"{len(c)}\n" + "".join(l + "\n" for l in c) for c in cases))
