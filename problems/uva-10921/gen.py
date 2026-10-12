"""UVa 10921 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10921-{kind}-{k}")
out = sys.stdout.write

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def expr():
    n = rng.randint(1, 30)
    return "".join(rng.choice(ALPHA * 4 + "--10") for _ in range(n))
lines = [expr() for _ in range(rng.randint(3, 40))]
if kind == "hidden" and k == 1:
    lines = ["A", "-", "1", "0", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "PQRS-WXYZ", "1-0-1-0", "Z" * 30]
out("".join(l + "\n" for l in lines))
