"""UVa 13190 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"13190-{kind}-{k}")
out = sys.stdout.write

import string
def case():
    n = rng.randint(1, 30)
    names = ["".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, 15))) for _ in range(n)]
    return f"{n} {rng.randint(1, 300)}\n" + "".join(f"{nm} {rng.randint(1, 40)}\n" for nm in names)
cases = [case() for _ in range(rng.randint(1, 5))]
out(f"{len(cases)}\n" + "".join(cases))
