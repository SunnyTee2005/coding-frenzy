"""UVa 11455 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11455-{kind}-{k}")
out = sys.stdout.write

qs = []
for _ in range(rng.randint(5, 300)):
    hi = rng.choice([5, 100, 2**30])
    r = rng.random()
    if r < 0.15:
        x = rng.randint(1, hi); q = [x] * 4
    elif r < 0.35:
        x, y = rng.randint(1, hi), rng.randint(1, hi); q = [x, x, y, y]
    elif r < 0.45:  # 最長邊剛好等於其他三邊和（退化）
        a, b, c = rng.randint(1, hi // 3 + 1), rng.randint(1, hi // 3 + 1), rng.randint(1, hi // 3 + 1); q = [a, b, c, a + b + c]
    else:
        q = [rng.randint(1, hi) for _ in range(4)]
    rng.shuffle(q)
    qs.append(q)
if kind == "hidden" and k == 1:
    qs = [[1, 1, 1, 1], [2**30] * 4, [1, 1, 1, 3], [1, 1, 1, 2], [1, 2, 1, 2], [2**30, 2**30, 2**30, 2**30 - 1], [1, 1, 2, 2]]
out(f"{len(qs)}\n" + "".join(" ".join(map(str, q)) + "\n" for q in qs))
