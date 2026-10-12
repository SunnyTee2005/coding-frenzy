"""UVa 145 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"145-{kind}-{k}")
out = sys.stdout.write

# 開始與結束時間相同時算 0 還是 24 小時題目沒講清楚，避開
calls = []
while len(calls) < rng.randint(3, 200):
    h1, m1, h2, m2 = rng.randint(0, 23), rng.randint(0, 59), rng.randint(0, 23), rng.randint(0, 59)
    if (h1, m1) == (h2, m2):
        continue
    num = f"{rng.randint(0, 999):03d}-{rng.randint(0, 9999):04d}"
    calls.append(f"{rng.choice('ABCDE')} {num} {h1:02d} {m1:02d} {h2:02d} {m2:02d}")
if kind == "hidden" and k == 1:
    calls = ["A 183-5724 17 58 18 04", "E 999-9999 08 00 07 59", "B 000-0000 21 59 22 00", "C 123-4567 07 59 08 00",
             "D 555-1234 23 00 01 00", "E 111-2222 18 00 17 59"]
out("".join(c + "\n" for c in calls) + "#\n")
