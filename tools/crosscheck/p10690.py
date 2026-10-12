"""UVa 10690 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    p, res = 0, []
    while p < len(v):
        n, m = v[p], v[p + 1]
        a = v[p + 2:p + 2 + n + m]
        p += 2 + n + m
        total = sum(a)
        k = min(n, m)
        # sums[c] = 選 c 個數可以得到的所有總和
        sums = [set() for _ in range(k + 1)]
        sums[0].add(0)
        for x in a:
            for c in range(k, 0, -1):
                sums[c] |= {t + x for t in sums[c - 1]}
        vals = [t * (total - t) for t in sums[k]]
        res.append(f"{max(vals)} {min(vals)}")
    return "\n".join(res) + "\n"
