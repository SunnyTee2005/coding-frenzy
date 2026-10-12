"""UVa 458 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"458-{kind}-{k}")
out = sys.stdout.write

# 原文用可印字元（到 'x' 為止，編碼後仍是 ASCII）
CH = "".join(chr(c) for c in range(32, 121))
WORDS = ["the", "trademark", "of", "Corporation.", "*IBM", "is", "a", "Hello,", "world!", "CPE", "2026", "(test)", "x"]
lines = []
for _ in range(rng.randint(1, 80)):
    if rng.random() < 0.6:
        plain = " ".join(rng.choice(WORDS) for _ in range(rng.randint(1, 12)))
    else:
        plain = "".join(rng.choice(CH) for _ in range(rng.randint(1, 80)))
    lines.append("".join(chr(ord(c) + 7) for c in plain))
out("".join(l + "\n" for l in lines))
