"""UVa 11541 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11541-{kind}-{k}")
out = sys.stdout.write

def case():
    parts, total = [], 0
    while total < 200:
        n = rng.choice([1, 1, 2, 3, 9, 10, 12, 25])
        if total + n > 200: break
        parts.append(rng.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(n)); total += n
        if rng.random() < 0.15: break
    return "".join(parts) or "A1"
T = 49 if kind == "hidden" and k >= 8 else rng.randint(3, 20)
cases = [case() for _ in range(T)]
if kind == "hidden" and k == 1:
    cases = ["A1", "Z200", "A1B1C1", "Q10R01", "A9B10C11"]
out(f"{len(cases)}\n" + "".join(c + "\n" for c in cases))
