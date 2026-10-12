"""UVa 12592 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12592-{kind}-{k}")
out = sys.stdout.write

def phrase():
    words = ["".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 8))) for _ in range(rng.randint(1, 6))]
    return " ".join(words)[:100]
n = rng.randint(1, 20)
firsts = []
while len(firsts) < n:
    p = phrase()
    if p not in firsts:
        firsts.append(p)
pairs = [(f, phrase()) for f in firsts]
qs = [rng.choice(firsts) for _ in range(rng.randint(1, 100))]
out(f"{n}\n" + "".join(f"{a}\n{b}\n" for a, b in pairs) + f"{len(qs)}\n" + "".join(q + "\n" for q in qs))
