"""UVa 10935 測資：python3 gen.py <public|hidden> <編號>"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10935-{kind}-{k}")
if kind == "hidden" and k == 1:
    ns = [1]  # n = 1：「Discarded cards:」後面不能有空白
elif kind == "hidden" and k == 2:
    ns = list(range(1, 51))
else:
    ns = [rng.randint(1, 50) for _ in range(rng.randint(1, 30))]
sys.stdout.write("".join(f"{n}\n" for n in ns) + "0\n")
