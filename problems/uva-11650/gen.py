"""UVa 11650 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11650-{kind}-{k}")
out = sys.stdout.write

times = [(rng.randint(1, 12), rng.randint(0, 59)) for _ in range(rng.randint(3, 40))]
if kind == "hidden" and k == 1:
    times = [(h, m) for h in (12, 1, 6, 11) for m in (0, 1, 30, 59)]
if kind == "hidden" and k == 2:
    times = [(h, m) for h in range(1, 13) for m in range(60)]
out(f"{len(times)}\n" + "".join(f"{h:02d}:{m:02d}\n" for h, m in times))
