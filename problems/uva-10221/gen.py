"""UVa 10221 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10221-{kind}-{k}")
out = sys.stdout.write

# 角度超過 180 度時要不要取 360-a，題目沒有講，測資只出 0~180 度
qs = []
for _ in range(rng.randint(5, 200)):
    s = rng.randint(0, rng.choice([1000, 100000]))
    if rng.random() < 0.5:
        qs.append((s, rng.randint(0, 180), "deg"))
    else:
        qs.append((s, rng.randint(0, 10800), "min"))
if kind == "hidden" and k == 1:
    qs = [(0, 0, "deg"), (0, 180, "deg"), (0, 10800, "min"), (1, 1, "min"), (100000, 90, "deg")]
out("".join(f"{s} {a} {u}\n" for s, a, u in qs))
