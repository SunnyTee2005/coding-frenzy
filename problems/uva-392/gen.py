"""UVa 392 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"392-{kind}-{k}")
out = sys.stdout.write

def poly():
    return [rng.choice([0, 0, 0, 1, -1, rng.randint(-1000, 1000)]) for _ in range(9)]
ps = [poly() for _ in range(rng.randint(3, 80))]
if kind == "hidden" and k == 1:
    ps = [[0] * 9, [0] * 8 + [1], [0] * 8 + [-1], [0] * 7 + [1, 0], [0] * 7 + [-1, 0], [1] + [0] * 8, [-1] + [0] * 8, [-5, 0, 0, 0, 0, 0, 0, 0, 7]]
out("".join(" ".join(map(str, p)) + "\n" for p in ps))
