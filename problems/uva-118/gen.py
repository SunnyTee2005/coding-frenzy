"""UVa 118 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"118-{kind}-{k}")
out = sys.stdout.write

mx, my = rng.randint(0, 50 if k > 3 else 6), rng.randint(0, 50 if k > 3 else 6)
robots = []
for _ in range(rng.randint(1, 60)):
    cmd = "".join(rng.choice("LRFFF") for _ in range(rng.randint(1, 99)))
    robots.append((rng.randint(0, mx), rng.randint(0, my), rng.choice("NESW"), cmd))
if kind == "hidden" and k == 1:
    mx, my = 0, 0
    robots = [(0, 0, "N", "F"), (0, 0, "N", "F"), (0, 0, "E", "FLF"), (0, 0, "S", "RRF"), (0, 0, "W", "L")]
out(f"{mx} {my}\n" + "".join(f"{x} {y} {o}\n{c}\n" for x, y, o, c in robots))
