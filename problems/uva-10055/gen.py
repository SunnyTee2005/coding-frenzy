"""產生 UVa 10055 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10055-{kind}-{k}")
MAX = 2**32

if kind == "public":
    lines = [(rng.randint(0, 1000), rng.randint(0, 1000)) for _ in range(5 * k)]
elif k == 1:
    # 邊界：0 與 2^32、兩數相等、大小順序顛倒
    lines = [(0, 0), (0, MAX), (MAX, 0), (MAX, MAX), (1, 0), (12345, 12345)]
elif k == 2:
    # 只有一行、沒有結尾換行
    sys.stdout.write(f"{MAX} 1")
    sys.exit()
elif k <= 6:
    lines = [(rng.randint(0, MAX), rng.randint(0, MAX)) for _ in range(1000)]
else:
    # 大量資料
    lines = [(rng.randint(0, MAX), rng.randint(0, MAX)) for _ in range(20000)]

sys.stdout.write("".join(f"{a} {b}\n" for a, b in lines))
