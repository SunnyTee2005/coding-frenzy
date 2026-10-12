"""UVa 10125 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import combinations

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    p, res = 0, []
    while v[p] != 0:
        n = v[p]
        a = v[p + 1:p + 1 + n]
        p += 1 + n
        best = None
        if n <= 30:
            for d in a:
                for x, y, z in combinations([e for e in a if e != d], 3):
                    if x + y + z == d and (best is None or d > best):
                        best = d
        else:
            pairs = {}
            for i, j in combinations(range(n), 2):
                pairs.setdefault(a[i] + a[j], []).append((i, j))
            for di in range(n):
                for ci in range(n):
                    if ci == di or (best is not None and a[di] <= best):
                        continue
                    for i, j in pairs.get(a[di] - a[ci], []):
                        if len({i, j, ci, di}) == 4:
                            best = a[di]
                            break
        res.append("no solution" if best is None else str(best))
    return "\n".join(res) + "\n"
