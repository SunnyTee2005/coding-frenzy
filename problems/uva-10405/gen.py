"""UVa 10405 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10405-{kind}-{k}")
out = sys.stdout.write

pairs = []
for _ in range(rng.randint(1, 15)):
    al = rng.choice(["ab", "abcd", "abcdefghijklmnopqrstuvwxyz0123456789", "a b c"])
    la, lb = rng.randint(1, 60), rng.randint(1, 60)
    if kind == "hidden" and k == 10 and not pairs:
        la, lb = 1000, 1000
    pairs.append(("".join(rng.choice(al) for _ in range(la)), "".join(rng.choice(al) for _ in range(lb))))
if kind == "hidden" and k == 1:
    pairs = [("a", "a"), ("a", "b"), ("abc", "cba"), ("x", "xxxxx")]
out("".join(f"{a}\n{b}\n" for a, b in pairs))
