"""UVa 10813 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10813-{kind}-{k}")
out = sys.stdout.write

games = []
for _ in range(rng.randint(1, 30)):
    cols = [rng.sample(range(15 * c + 1, 15 * c + 16), 5) for c in range(5)]
    rows = [[cols[c][r] for c in range(5) if not (r == 2 and c == 2)] for r in range(5)]
    order = list(range(1, 76)); rng.shuffle(order)
    games.append((rows, order))
def fmt(order):
    out_lines, i = [], 0
    while i < 75:
        w = rng.choice([75, 10, 15, 25, 1])
        out_lines.append(" ".join(map(str, order[i:i + w]))); i += w
    return "".join(l + "\n" for l in out_lines)
out(f"{len(games)}\n" + "".join("".join(" ".join(map(str, r)) + "\n" for r in rows) + fmt(order) for rows, order in games))
