"""UVa 10252 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10252-{kind}-{k}")
out = sys.stdout.write

def w():
    return "".join(rng.choice("abcdefghij" if rng.random() < 0.5 else "abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(0, 1000 if k == 10 else 20)))
pairs = [(w(), w()) for _ in range(rng.randint(2, 40))]
if kind == "hidden" and k == 1:
    pairs = [("", ""), ("abc", ""), ("", "abc"), ("aaa", "aa"), ("xyz", "abc")]
out("".join(f"{a}\n{b}\n" for a, b in pairs))
