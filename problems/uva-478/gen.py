"""UVa 478 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"478-{kind}-{k}")
out = sys.stdout.write

from fractions import Fraction as F
def r1():
    return round(rng.uniform(-20, 30), 1)
figs = []
for _ in range(rng.randint(1, 10)):
    t = rng.choice("rct")
    if t == "r":
        x1, x2 = sorted([r1(), r1()]); y2, y1 = sorted([r1(), r1()])
        if x1 == x2 or y1 == y2: continue
        figs.append(("r", [x1, y1, x2, y2]))
    elif t == "c":
        figs.append(("c", [r1(), r1(), round(rng.uniform(0.5, 15), 1)]))
    else:
        pts = [r1() for _ in range(6)]
        area = (pts[2] - pts[0]) * (pts[5] - pts[1]) - (pts[3] - pts[1]) * (pts[4] - pts[0])
        if abs(area) < 1: continue
        figs.append(("t", pts))
if not figs:
    figs = [("c", [0.0, 0.0, 5.0])]
def on_boundary(x, y):
    # 用分數精確判斷是否剛好在邊界上（題目沒有定義邊界，所以不出這種點）
    X, Y = F(str(x)), F(str(y))
    for t, v in figs:
        V = [F(str(a)) for a in v]
        if t == "r":
            if (X in (V[0], V[2]) and V[3] <= Y <= V[1]) or (Y in (V[1], V[3]) and V[0] <= X <= V[2]): return True
        elif t == "c":
            if (X - V[0]) ** 2 + (Y - V[1]) ** 2 == V[2] ** 2: return True
        else:
            for (ax, ay), (bx, by) in [((V[0], V[1]), (V[2], V[3])), ((V[2], V[3]), (V[4], V[5])), ((V[4], V[5]), (V[0], V[1]))]:
                if (bx - ax) * (Y - ay) - (by - ay) * (X - ax) == 0 and min(ax, bx) <= X <= max(ax, bx) and min(ay, by) <= Y <= max(ay, by): return True
    return False
pts = []
while len(pts) < rng.randint(3, 60):
    x, y = r1(), r1()
    if not on_boundary(x, y):
        pts.append((x, y))
def fmt(v):
    return f"{v:.1f}"
out("".join(f"{t} " + " ".join(fmt(a) for a in v) + "\n" for t, v in figs) + "*\n")
out("".join(f"{fmt(x)} {fmt(y)}\n" for x, y in pts) + "9999.9 9999.9\n")
