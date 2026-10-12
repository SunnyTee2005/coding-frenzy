"""UVa 10327 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10327-{kind}-{k}")
out = sys.stdout.write

def case():
    n = rng.randint(1, 1000 if (kind == "hidden" and k >= 9) else 30)
    return f"{n}\n" + " ".join(str(rng.randint(-1000, 1000)) for _ in range(n)) + "\n"
cases = [case() for _ in range(rng.randint(1, 6))]
if kind == "hidden" and k == 1:
    cases = ["1\n5\n", "2\n2 1\n", "5\n5 4 3 2 1\n", "4\n1 1 1 1\n", "3\n3 1 2\n"]
out("".join(cases))
