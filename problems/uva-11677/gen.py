"""UVa 11677 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11677-{kind}-{k}")
out = sys.stdout.write

qs = []
while len(qs) < rng.randint(5, 300):
    q = (rng.randint(0, 23), rng.randint(0, 59), rng.randint(0, 23), rng.randint(0, 59))
    if q[:2] != q[2:]:  # 現在時間等於鬧鐘時間時答案是 0 還是 1440，題目沒講，避開
        qs.append(q)
if kind == "hidden" and k == 1:
    qs = [(0, 0, 23, 59), (23, 59, 0, 0), (0, 0, 0, 1), (0, 1, 0, 0), (12, 0, 12, 1)]
out("".join(" ".join(map(str, q)) + "\n" for q in qs) + "0 0 0 0\n")
