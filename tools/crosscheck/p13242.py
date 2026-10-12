"""UVa 13242 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from fractions import Fraction

def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        cap, target, n = next(it), next(it), next(it)
        jars = [(next(it), next(it)) for _ in range(n)]
        pre_v, pre_h = [0], [0]
        for v, t in jars:
            pre_v.append(pre_v[-1] + v)
            pre_h.append(pre_h[-1] + v * t)
        best = None
        for i in range(n):
            for j in range(i, n):
                vol = pre_v[j + 1] - pre_v[i]
                if vol > cap:
                    break
                if 2 * vol < cap:
                    continue
                d = abs(Fraction(pre_h[j + 1] - pre_h[i], vol) - target)
                if d <= 5 and (best is None or d < best[0]):
                    best = (d, i, j)
        res.append("Not possible" if best is None else f"{best[1]} {best[2]}")
    return "\n".join(res) + "\n"
