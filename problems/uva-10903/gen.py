"""UVa 10903 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10903-{kind}-{k}")
out = sys.stdout.write

M = ["rock", "paper", "scissors"]
cases = []
for _ in range(rng.randint(1, 4)):
    n, kk = rng.randint(1, 8), rng.randint(1, 5)
    if kind == "hidden" and k == 10:
        n, kk = 30, 3
    games = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for _ in range(kk):
                a, b = (i, j) if rng.random() < 0.5 else (j, i)
                same = rng.random() < 0.2
                ma = rng.choice(M)
                games.append((a, ma, b, ma if same else rng.choice(M)))
    rng.shuffle(games)
    cases.append((n, kk, games))
if kind == "hidden" and k == 1:
    cases = [(1, 5, []), (2, 1, [(1, "rock", 2, "rock")]), (3, 1, [(1, "rock", 2, "scissors"), (3, "paper", 1, "rock"), (2, "paper", 3, "scissors")])]
out("".join(f"{n} {kk}\n" + "".join(f"{a} {ma} {b} {mb}\n" for a, ma, b, mb in g) for n, kk, g in cases) + "0\n")
