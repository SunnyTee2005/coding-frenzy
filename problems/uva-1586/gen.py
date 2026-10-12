"""UVa 1586 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1586-{kind}-{k}")
out = sys.stdout.write

def formula():
    parts = []
    for _ in range(rng.randint(1, 12)):
        e = rng.choice("CHON")
        n = rng.choice([0, 0, 1, 2, 3, 5, 12, 22, 99])
        parts.append(e + ("" if n == 0 else str(n)))
    return "".join(parts)[:80]
fs = [formula() for _ in range(rng.randint(3, 60))]
if kind == "hidden" and k == 1:
    fs = ["C", "H", "O", "N", "C99H99O99N99", "H2O", "CO2"]
out(f"{len(fs)}\n" + "".join(f + "\n" for f in fs))
