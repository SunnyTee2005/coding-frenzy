"""UVa 941 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"941-{kind}-{k}")
out = sys.stdout.write

# 只用不重複的字母（重複字母時怎麼算排列，題目原文才說得清楚）
from math import factorial
cases = []
for _ in range(rng.randint(1, 100)):
    n = rng.randint(1, 20)
    s = "".join(rng.sample("abcdefghijklmnopqrstuvwxyz", n))
    cases.append((s, rng.randint(0, factorial(n) - 1)))
if kind == "hidden" and k == 1:
    cases = [("a", 0), ("ba", 1), ("abcdefghijklmnopqrst", 2432902008176639999), ("abcdefghijklmnopqrst", 0)]
out(f"{len(cases)}\n" + "".join(f"{s}\n{n}\n" for s, n in cases))
