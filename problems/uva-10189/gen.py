"""UVa 10189 測資：python3 gen.py <public|hidden> <編號>"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10189-{kind}-{k}")


def field(n, m, p):
    return f"{n} {m}\n" + "".join("".join("*" if rng.random() < p else "." for _ in range(m)) + "\n" for _ in range(n))


parts = []
if kind == "hidden" and k == 1:
    # 邊界：1x1、全是地雷、沒有地雷、單列、單行
    parts = ["1 1\n*\n", "1 1\n.\n", field(3, 3, 1.0), field(4, 5, 0.0), field(1, 30, 0.3), field(30, 1, 0.3)]
elif kind == "hidden" and k == 2:
    parts = ["1 1\n.\n"]  # 只有一個場地：不能多印空行
elif kind == "hidden" and k >= 8:
    parts = [field(100, 100, rng.random()) for _ in range(4)]
else:
    parts = [field(rng.randint(1, 12), rng.randint(1, 12), rng.random() * 0.5) for _ in range(rng.randint(1, 8))]
sys.stdout.write("".join(parts) + "0 0\n")
