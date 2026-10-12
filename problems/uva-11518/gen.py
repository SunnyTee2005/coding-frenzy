"""UVa 11518 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11518-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 8)):
    n = rng.randint(1, 50 if k < 10 else 2000)
    edges = [(rng.randint(1, n), rng.randint(1, n)) for _ in range(rng.randint(0, 2 * n))]
    knocks = [rng.randint(1, n) for _ in range(rng.randint(1, 5))]
    cases.append((n, edges, knocks))
out(f"{len(cases)}\n" + "".join(f"{n} {len(e)} {len(z)}\n" + "".join(f"{x} {y}\n" for x, y in e) + "".join(f"{x}\n" for x in z)
                             for n, e, z in cases))
