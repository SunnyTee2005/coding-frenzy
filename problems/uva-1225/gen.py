"""UVa 1225 測資：python3 gen.py <public|hidden> <編號>"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1225-{kind}-{k}")
if kind == "hidden" and k == 1:
    ns = [1, 9, 10, 11, 99, 100, 101, 999, 1000, 9999]
elif kind == "hidden" and k >= 6:
    ns = [rng.randint(5000, 9999) for _ in range(20)]
else:
    ns = [rng.randint(1, 10 ** rng.randint(1, 4) - 1) for _ in range(rng.randint(1, 20))]
sys.stdout.write(f"{len(ns)}\n" + "".join(f"{n}\n" for n in ns))
