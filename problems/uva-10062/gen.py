"""UVa 10062 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10062-{kind}-{k}")
out = sys.stdout.write

# 空行要不要輸出一個空的區塊題目沒講，不出空行
CH = "".join(chr(c) for c in range(32, 127))
lines = []
for _ in range(rng.randint(1, 40)):
    pool = rng.choice([CH, "AAABBC", "122333 ", "abcABC"])
    lines.append("".join(rng.choice(pool) for _ in range(rng.randint(1, 1000 if k == 10 else 60))))
if kind == "hidden" and k == 1:
    lines = [" ", "~", "a", "ba", "ab", "aabb"]
out("".join(l + "\n" for l in lines))
