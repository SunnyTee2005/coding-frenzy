"""UVa 11039 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11039-{kind}-{k}")
out = sys.stdout.write

def case():
    n = rng.randint(1, 2500 if k == 10 else 40)
    sizes = rng.sample(range(1, 999999), n)
    return f"{n}\n" + "".join(f"{s if rng.random() < 0.5 else -s}\n" for s in sizes)
cases = [case() for _ in range(rng.randint(1, 5))]
if kind == "hidden" and k == 1:
    cases = ["1\n5\n", "1\n-5\n", "2\n3\n4\n", "2\n3\n-4\n", "4\n1\n-2\n3\n-4\n"]
out(f"{len(cases)}\n" + "".join(cases))
