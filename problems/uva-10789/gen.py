"""UVa 10789 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10789-{kind}-{k}")
out = sys.stdout.write

A = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ss = []
for _ in range(rng.randint(1, 60 if k < 10 else 30)):
    pool = rng.sample(A, rng.randint(1, 62))
    ss.append("".join(rng.choice(pool) for _ in range(rng.randint(1, 2000 if k == 10 else 60))))
if kind == "hidden" and k == 1:
    ss = ["a", "aa", "aaa", "aaaa", "Aa0Aa0", "z" * 2000, "1" * 997]
out(f"{len(ss)}\n" + "".join(s + "\n" for s in ss))
