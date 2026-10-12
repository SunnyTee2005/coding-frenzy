"""UVa 10672 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10672-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 5)):
    n = rng.randint(1, 20 if k < 10 else 2000)
    label = list(range(1, n + 1)); rng.shuffle(label)
    children = {i: [] for i in range(n)}
    for i in range(1, n):
        children[rng.randint(max(0, i - rng.choice([1, 4, i])), i - 1)].append(i)
    marbles = [0] * n
    for _ in range(n):  # 總數等於 n
        marbles[rng.randrange(n) if rng.random() < 0.7 else 0] += 1
    lines = [f"{label[i]} {marbles[i]} {len(children[i])}" + "".join(f" {label[c]}" for c in children[i]) for i in range(n)]
    rng.shuffle(lines)
    cases.append(lines)
out("".join(f"{len(c)}\n" + "".join(l + "\n" for l in c) for c in cases) + "0\n")
