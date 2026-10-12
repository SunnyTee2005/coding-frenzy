"""UVa 412 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"412-{kind}-{k}")
out = sys.stdout.write

def case():
    n = rng.randint(1, 50)
    if rng.random() < 0.1:
        v = [2 * rng.randint(1, 20000) for _ in range(n)]
    else:
        v = [rng.randint(1, 32767) for _ in range(n)]
    return f"{n}\n" + "".join(f"{x}\n" for x in v)
cases = [case() for _ in range(rng.randint(1, 15))]
if kind == "hidden" and k == 1:
    cases = ["1\n7\n", "2\n4\n6\n", "2\n1\n1\n", "3\n2\n4\n6\n"]
out("".join(cases) + "0\n")
