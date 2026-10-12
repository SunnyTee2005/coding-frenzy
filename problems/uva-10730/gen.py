"""UVa 10730 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10730-{kind}-{k}")
out = sys.stdout.write

def anti(n):
    # 遞迴建構反等差排列：偶數放前、奇數放後
    if n == 1: return [0]
    a = anti((n + 1) // 2); b = anti(n // 2)
    return [2 * x for x in a] + [2 * x + 1 for x in b]
cases = []
for _ in range(rng.randint(3, 20)):
    n = rng.randint(3, 1000 if k >= 9 else 30)
    p = anti(n) if rng.random() < 0.5 else rng.sample(range(n), n)
    cases.append(p)
if kind == "hidden" and k == 1:
    cases = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [2, 0, 1, 3]]
out("".join(f"{len(p)}: " + " ".join(map(str, p)) + "\n" for p in cases) + "0\n")
