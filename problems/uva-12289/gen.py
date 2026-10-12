"""UVa 12289 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12289-{kind}-{k}")
out = sys.stdout.write

def typo(word):
    w = list(word)
    if rng.random() < 0.6:
        i = rng.randrange(len(w))
        w[i] = rng.choice([c for c in "abcdefghijklmnopqrstuvwxyz" if c != w[i]])
    return "".join(w)
n = 10 if kind == "hidden" else rng.randint(3, 10)
words = [typo(rng.choice(["one", "two", "three"])) for _ in range(n)]
if kind == "hidden" and k == 1:
    words = ["one", "two", "three", "onx", "xne", "twx", "xwo", "ttree", "threx", "oxe"]
out(f"{len(words)}\n" + "".join(w + "\n" for w in words))
