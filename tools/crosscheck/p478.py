"""UVa 478 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from fractions import Fraction as F

def solve(s: str) -> str:
    lines = s.splitlines()
    figs, i = [], 0
    while lines[i].strip() != "*":
        t, *v = lines[i].split(); figs.append((t, [F(x) for x in v])); i += 1
    i += 1
    res, pid = [], 0
    for line in lines[i:]:
        x, y = (F(a) for a in line.split())
        if x == F("9999.9") and y == F("9999.9"):
            break
        pid += 1
        hits = []
        for j, (t, v) in enumerate(figs, 1):
            if t == "r":
                ok = v[0] < x < v[2] and v[3] < y < v[1]
            elif t == "c":
                ok = (x - v[0]) ** 2 + (y - v[1]) ** 2 < v[2] ** 2
            else:
                ds = [(v[(2 * a + 2) % 6] - v[2 * a]) * (y - v[2 * a + 1]) - (v[(2 * a + 3) % 6] - v[2 * a + 1]) * (x - v[2 * a]) for a in range(3)]
                ok = all(d > 0 for d in ds) or all(d < 0 for d in ds)
            if ok:
                hits.append(f"Point {pid} is contained in figure {j}")
        res.extend(hits or [f"Point {pid} is not contained in any figure"])
    return "\n".join(res) + "\n"
