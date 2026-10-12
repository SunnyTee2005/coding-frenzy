"""UVa 10056 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10056-{kind}-{k}")
out = sys.stdout.write

# p = 0 時答案是 0 還是其他（0/0），題目沒講，避開
qs = []
for _ in range(rng.randint(1, 300)):
    n = rng.randint(1, 1000 if rng.random() < 0.3 else 10)
    p = rng.choice([rng.randint(1, 1000000) / 1000000, rng.randint(1, 100) / 100, 1.0])
    qs.append((n, f"{p:.6f}".rstrip("0").rstrip(".") if rng.random() < 0.5 else f"{p:.6f}", rng.randint(1, n)))
if kind == "hidden" and k == 1:
    qs = [(1, "0.5", 1), (1, "1", 1), (3, "1.0", 2), (1000, "0.000001", 1000), (1000, "0.000001", 1)]
out(f"{len(qs)}\n" + "".join(f"{n} {p} {i}\n" for n, p, i in qs))
