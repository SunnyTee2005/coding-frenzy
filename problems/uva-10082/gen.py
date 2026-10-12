"""UVa 10082 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10082-{kind}-{k}")
out = sys.stdout.write

ROWS = ["`1234567890-=", "QWERTYUIOP[]\\", "ASDFGHJKL;'", "ZXCVBNM,./"]
enc = {r[i]: r[i + 1] for r in ROWS for i in range(len(r) - 1)}
plain = "".join(enc)  # 每列除了最右邊的鍵都可以是原文
lines = []
for _ in range(rng.randint(1, 100)):
    text = "".join(rng.choice(plain) if rng.random() < 0.85 else " " for _ in range(rng.randint(1, 70)))
    lines.append("".join(enc.get(ch, ch) for ch in text))
if kind == "hidden" and k == 1:
    lines = ["1", "=", "W", "]", "\\", "S", "'", "X", "/", " "]
out("".join(l + "\n" for l in lines))
