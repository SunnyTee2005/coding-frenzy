"""UVa 11233 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11233-{kind}-{k}")
out = sys.stdout.write

STEMS = ["rice", "lobster", "berry", "turkey", "peach", "dish", "box", "bus", "potato", "day", "fly", "cherry", "key",
         "match", "brush", "fox", "kiss", "zoo", "toy", "baby", "car", "bach", "ash", "cy", "oy", "yy", "chy"]
def word():
    if rng.random() < 0.6:
        return rng.choice(STEMS)
    w = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 17)))
    return w + rng.choice(["", "y", "ch", "sh", "x", "o", "s", "ay", "ey"])
irr = {}
for _ in range(rng.randint(0, 20)):
    w = word()
    if len(w) <= 20:
        irr[w] = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 20)))
words = [w for w in (word() for _ in range(rng.randint(1, 100))) if 2 <= len(w) <= 20] or ["box"]
if kind == "hidden" and k == 1:
    irr = {}
    words = ["ay", "by", "ch", "sh", "x", "o", "s", "a", "chy"]
out(f"{len(irr)} {len(words)}\n" + "".join(f"{a} {b}\n" for a, b in irr.items()) + "".join(w + "\n" for w in words))
