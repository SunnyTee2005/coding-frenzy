"""UVa 11624 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11624-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 8)):
    r, c = rng.randint(1, 20), rng.randint(1, 20)
    if kind == "hidden" and k == 10 and not cases:
        r, c = 150, 150
    wall = rng.choice([0.0, 0.2, 0.35])
    g = [["#" if rng.random() < wall else "." for _ in range(c)] for _ in range(r)]
    for _ in range(rng.choice([0, 1, 1, 2, 5])):
        g[rng.randrange(r)][rng.randrange(c)] = "F"
    jr, jc = rng.randrange(r), rng.randrange(c)
    g[jr][jc] = "J"
    cases.append(["".join(row) for row in g])
if kind == "hidden" and k == 1:
    cases = [["J"], ["###", "#J#", "###"], ["#####", "#F.J#", "#####"], ["...", ".J.", "..F"], ["#.#", "#J#", "#F#"]]
out(f"{len(cases)}\n" + "".join(f"{len(g)} {len(g[0])}\n" + "".join(row + "\n" for row in g) for g in cases))
