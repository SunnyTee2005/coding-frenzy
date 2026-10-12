"""UVa 12820 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12820-{kind}-{k}")
out = sys.stdout.write

def word():
    alpha = rng.choice(["ab", "abc", "abcdef", "abcdefghijklmnopqrstuvwxyz"])
    return "".join(rng.choice(alpha) for _ in range(rng.randint(1, 30)))
cases = [[word() for _ in range(rng.randint(1, 60))] for _ in range(rng.randint(1, 10))]
if kind == "hidden" and k == 1:
    cases = [["a", "aa", "ab", "aab", "abc", "mammal", "needed", "papaya", "referee", "senselessness", "banana"]]
out("".join(f"{len(c)}\n" + "".join(w + "\n" for w in c) for c in cases))
