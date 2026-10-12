"""UVa 1339 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1339-{kind}-{k}")
out = sys.stdout.write

pairs = []
for _ in range(rng.randint(3, 150)):
    n = rng.randint(1, 100)
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:rng.randint(1, 26)]
    b = "".join(rng.choice(al) for _ in range(n))
    if rng.random() < 0.5:  # 真的加密：替換再排列
        perm = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"); rng.shuffle(perm)
        a = [perm[ord(c) - 65] for c in b]; rng.shuffle(a); a = "".join(a)
        if rng.random() < 0.3 and n > 1:  # 改一個字，通常就不成立
            i = rng.randrange(n); a = a[:i] + rng.choice(al) + a[i + 1:]
    else:
        a = "".join(rng.choice(al) for _ in range(n))
    pairs.append((a, b))
if kind == "hidden" and k == 1:
    pairs = [("A", "Z"), ("AB", "AA"), ("AAB", "BBA"), ("ABC", "CAB"), ("AABB", "ABCD")]
out("".join(f"{a}\n{b}\n" for a, b in pairs))
