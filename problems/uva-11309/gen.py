"""UVa 11309 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11309-{kind}-{k}")
out = sys.stdout.write

times = [(rng.randint(0, 23), rng.randint(0, 59)) for _ in range(rng.randint(3, 60))]
if kind == "hidden" and k == 1:
    times = [(23, 59), (0, 0), (0, 9), (0, 10), (9, 59), (11, 10), (12, 21), (22, 22), (23, 32), (13, 31)]
if kind == "hidden" and k == 2:
    times = [(h, m) for h in range(24) for m in range(0, 60, 7)]
out(f"{len(times)}\n" + "".join(f"{h:02d}:{m:02d}\n" for h, m in times))
