"""UVa 10038 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10038-{kind}-{k}")
out = sys.stdout.write

seqs = []
for _ in range(rng.randint(3, 60)):
    n = rng.randint(1, 3000 if (kind == "hidden" and k == 10 and not seqs) else 40)
    if rng.random() < 0.5:  # 造一個 jolly 序列：差值 1..n-1 隨機排列、隨機正負號
        diffs = list(range(1, n)); rng.shuffle(diffs)
        x = rng.randint(-1000, 1000); seq = [x]
        for d in diffs:
            x += d if rng.random() < 0.5 else -d
            seq.append(x)
        if rng.random() < 0.3 and n > 2:
            seq[rng.randrange(n)] += rng.choice([-1, 1])
    else:
        seq = [rng.randint(-50, 50) for _ in range(n)]
    seqs.append(seq)
if kind == "hidden" and k == 1:
    seqs = [[5], [1, 2], [1, 1], [2, 1], [1, 3], [3, 1, 2], [1, 2, 4]]
out("".join(f"{len(q)} {' '.join(map(str, q))}\n" for q in seqs))
