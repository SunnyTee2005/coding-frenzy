"""UVa 11576 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11576-{kind}-{k}")
out = sys.stdout.write

def case():
    kk = rng.randint(1, 8 if k < 8 else 100)
    alpha = "AB" if rng.random() < 0.5 else "ABCDE"
    words = ["".join(rng.choice(alpha) for _ in range(kk))]
    w = rng.randint(1, 30 if kind == "public" else 200)
    for _ in range(w - 1):
        # 讓下一個字和上一個字有一段重疊
        m = rng.randint(0, kk)
        words.append(words[-1][kk - m:] + "".join(rng.choice(alpha) for _ in range(kk - m)))
    return f"{kk} {len(words)}\n" + "".join(x + "\n" for x in words)
T = rng.randint(1, 8)
if kind == "hidden" and k == 1:
    out("4\n1 1\nA\n1 2\nA\nA\n2 3\nAB\nBA\nAB\n3 2\nABC\nDEF\n")
else:
    out(f"{T}\n" + "".join(case() for _ in range(T)))
