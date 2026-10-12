"""UVa 10222 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10222-{kind}-{k}")
out = sys.stdout.write

ROWS = ["`1234567890-=", "qwertyuiop[]\\", "asdfghjkl;'", "zxcvbnm,./"]
enc = {}
for row in ROWS:
    for i in range(len(row) - 2):
        enc[row[i]] = row[i + 2]
plain_chars = "abcdefghijklmnopqrstuvwxyz12345678"
lines = []
for _ in range(rng.randint(1, 80)):
    words = ["".join(rng.choice(plain_chars if rng.random() < 0.1 else "abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 9)))
             for _ in range(rng.randint(1, 8))]
    e = " ".join("".join(enc[c] for c in w) for w in words)
    e = "".join(c.upper() if c.isalpha() and rng.random() < 0.15 else c for c in e)
    lines.append(e)
if kind == "hidden" and k == 1:
    lines = ["d", "D", "3", "]", "'", "/", "e r t"]
out(f"{len(lines)}\n" + "".join(l + "\n" for l in lines))
