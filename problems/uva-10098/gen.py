"""UVa 10098 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10098-{kind}-{k}")
out = sys.stdout.write

import math
def word():
    while True:
        alpha = rng.choice(["ab", "abc", "abcd", "abcdefgh", "aabbz"])
        w = "".join(rng.choice(alpha) for _ in range(rng.randint(1, 7)))
        from collections import Counter
        perms = math.factorial(len(w))
        for c in Counter(w).values():
            perms //= math.factorial(c)
        if perms * (len(w) + 1) < 8000:
            return w
ws = [word() for _ in range(rng.randint(1, 6))]
if kind == "hidden" and k == 1:
    ws = ["a", "aa", "ba", "aab", "zyx"]
out(f"{len(ws)}\n" + "".join(w + "\n" for w in ws))
