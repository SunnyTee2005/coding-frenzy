"""UVa 10409 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10409-{kind}-{k}")
out = sys.stdout.write

games = []
if kind == "hidden" and k == 10:
    games.append([rng.choice(["north", "east", "south", "west"]) for _ in range(1024)])
for _ in range(rng.randint(1, 30)):
    n = rng.randint(1, 20)
    games.append([rng.choice(["north", "east", "south", "west"]) for _ in range(n)])
out("".join(f"{len(g)}\n" + "".join(c + "\n" for c in g) for g in games) + "0\n")
