"""UVa 907 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    p, res = 0, []
    while p < len(v):
        n, k = v[p], v[p + 1]
        d = v[p + 2:p + 3 + n]
        p += 3 + n
        segs = n + 1
        days = min(k + 1, segs)
        pre = [0]
        for x in d:
            pre.append(pre[-1] + x)
        # best[j][i]：前 i 段分成 j 天的最小「單日最大距離」
        INF = float("inf")
        best = [[INF] * (segs + 1) for _ in range(days + 1)]
        best[0][0] = 0
        for j in range(1, days + 1):
            for i in range(1, segs + 1):
                for t in range(j - 1, i):
                    cand = max(best[j - 1][t], pre[i] - pre[t])
                    if cand < best[j][i]:
                        best[j][i] = cand
        res.append(str(best[days][segs]))
    return "\n".join(res) + "\n"
