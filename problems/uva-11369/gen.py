"""UVa 11369 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11369-{kind}-{k}")
out = sys.stdout.write

def case():
    n = rng.randint(1, 2000 if k == 10 else 40)
    return f"{n}\n" + " ".join(str(rng.randint(1, 20000)) for _ in range(n)) + "\n"
cases = [case() for _ in range(rng.randint(1, 8))]
if kind == "hidden" and k == 1:
    cases = ["1\n5\n", "2\n5 6\n", "3\n1 1 1\n", "6\n1 2 3 4 5 6\n"]
out(f"{len(cases)}\n" + "".join(cases))
