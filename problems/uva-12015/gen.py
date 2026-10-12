"""UVa 12015 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12015-{kind}-{k}")
out = sys.stdout.write

def url():
    return "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 10))) + rng.choice([".com", ".edu.tw", ".org", ".com.hk"])
cases = []
for _ in range(rng.randint(1, 60)):
    hi = rng.choice([2, 5, 100])
    cases.append([(("www." if rng.random() < 0.5 else "") + url(), rng.randint(1, hi)) for _ in range(10)])
out(f"{len(cases)}\n" + "".join("".join(f"{u} {v}\n" for u, v in c) for c in cases))
