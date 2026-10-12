"""UVa 417 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"417-{kind}-{k}")
out = sys.stdout.write

L = "abcdefghijklmnopqrstuvwxyz"
ws = []
for _ in range(rng.randint(5, 300)):
    n = rng.randint(1, 5)
    if rng.random() < 0.7:
        ws.append("".join(sorted(rng.sample(L, n))))
    else:
        ws.append("".join(rng.choice(L) for _ in range(n)))
if kind == "hidden" and k == 1:
    ws = ["a", "z", "ab", "aa", "ba", "vwxyz", "abcde", "yz", "abcdef"[:5], "zz"]
out("".join(w + "\n" for w in ws))
