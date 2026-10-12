"""UVa 340 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"340-{kind}-{k}")
out = sys.stdout.write

games = []
for _ in range(rng.randint(1, 5)):
    n = rng.randint(1, 20 if k < 10 else 1000)
    code = [rng.randint(1, 9) for _ in range(n)]
    guesses = []
    for _ in range(rng.randint(0, 15)):
        g = [x if rng.random() < 0.3 else rng.randint(1, 9) for x in code] if rng.random() < 0.5 else [rng.randint(1, 9) for _ in range(n)]
        guesses.append(g)
    games.append((code, guesses))
if kind == "hidden" and k == 1:
    games = [([1], [[1], [2]]), ([1, 2], [[2, 1], [1, 2], [3, 3]]), ([5, 5], [])]
out("".join(f"{len(c)}\n{' '.join(map(str, c))}\n" + "".join(" ".join(map(str, g)) + "\n" for g in gs) + " ".join(["0"] * len(c)) + "\n"
            for c, gs in games) + "0\n")
