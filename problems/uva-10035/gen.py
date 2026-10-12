"""UVa 10035 測資：python3 gen.py <public|hidden> <編號>"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10035-{kind}-{k}")
MAX = 999_999_999


def num(digits):
    return rng.randint(0, 10**digits - 1)


pairs = []
if kind == "hidden" and k == 1:
    # 邊界：0、連續進位、位數不同、最大值、恰好 1 次進位
    pairs = [(0, 1), (1, 0), (999999999, 1), (1, 999999999), (MAX, MAX), (5, 5), (123, 456), (55, 5), (9, 1), (0, 999)]
elif kind == "hidden" and k >= 8:
    pairs = [(num(rng.randint(1, 9)), num(rng.randint(1, 9))) for _ in range(5000)]
else:
    pairs = [(num(rng.randint(1, 9)), num(rng.randint(1, 9))) for _ in range(rng.randint(5, 200))]
pairs = [(a, b) for a, b in pairs if a or b]
sys.stdout.write("".join(f"{a} {b}\n" for a, b in pairs) + "0 0\n")
