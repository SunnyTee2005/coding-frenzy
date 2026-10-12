"""UVa 297 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"297-{kind}-{k}")
out = sys.stdout.write

def tree(depth):
    if depth == 5 or rng.random() < 0.3:
        return rng.choice("ef")
    return "p" + "".join(tree(depth + 1) for _ in range(4))
pairs = [(tree(0), tree(0)) for _ in range(rng.randint(1, 20))]
if kind == "hidden" and k == 1:
    pairs = [("e", "e"), ("f", "e"), ("e", "f"), ("f", "f"), ("pffff", "e"), ("peeee", "peeee")]
out(f"{len(pairs)}\n" + "".join(f"{a}\n{b}\n" for a, b in pairs))
