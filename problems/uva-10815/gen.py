"""UVa 10815 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10815-{kind}-{k}")
out = sys.stdout.write

VOCAB = ["the", "Sign", "READ", "disneyland", "a", "fork", "road", "Two", "blondes", "went", "home", "So", "they", "were",
         "going", "to", "when", "came", "in", "Adventures", "left", "it's", "don't", "x-ray", "e-mail", "abc123def", "Zebra", "zz"]
lines = []
for _ in range(rng.randint(1, 120)):
    ws = []
    for _ in range(rng.randint(0, 14)):
        w = rng.choice(VOCAB) if rng.random() < 0.7 else "".join(rng.choice("abcdefghijklmnopqrstuvwxyzABCDEFG") for _ in range(rng.randint(1, 8)))
        ws.append(w + rng.choice(["", "", ",", ".", "!", "\"", ")", "--"]))
    lines.append(rng.choice(["", " ", "\t"]) + " ".join(ws))
if kind == "hidden" and k == 1:
    lines = ["a", "A", "", "123 456", "a1b2c3", "...hello...World..."]
out("\n".join(lines) + "\n")
