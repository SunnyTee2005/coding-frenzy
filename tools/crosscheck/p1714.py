"""UVa 1714 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import heapq

def solve(s: str) -> str:
    tok = s.split()
    p, res = 0, []
    while p < len(tok):
        r, c = int(tok[p]), int(tok[p + 1])
        g = tok[p + 2:p + 2 + r]
        text = tok[p + 2 + r] + "*"
        p += 3 + r
        def move(i, j, di, dj):
            ni, nj = i, j
            while 0 <= ni < r and 0 <= nj < c and g[ni][nj] == g[i][j]:
                ni += di; nj += dj
            return (ni, nj) if 0 <= ni < r and 0 <= nj < c else (i, j)
        # 分層：dist 是打完前 k 個字、游標在各格時的最少按鍵數
        INF = float("inf")
        dist = {(i, j): INF for i in range(r) for j in range(c)}
        dist[(0, 0)] = 0
        for ch in text:
            # 從上一層各格（起始距離不同）出發的最短路：Dijkstra
            best = dict(dist)
            heap = [(d, cell) for cell, d in dist.items() if d < INF]
            heapq.heapify(heap)
            while heap:
                d, cell = heapq.heappop(heap)
                if d > best[cell]:
                    continue
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nb = move(cell[0], cell[1], di, dj)
                    if d + 1 < best[nb]:
                        best[nb] = d + 1
                        heapq.heappush(heap, (d + 1, nb))
            dist = {cell: (best[cell] + 1 if g[cell[0]][cell[1]] == ch else INF) for cell in best}
        res.append(str(min(dist.values())))
    return "\n".join(res) + "\n"
