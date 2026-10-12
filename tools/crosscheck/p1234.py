"""UVa 1234 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import heapq

def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        n, m = next(it), next(it)
        adj = [[] for _ in range(n + 1)]
        total = 0
        for _ in range(m):
            a, b, c = next(it), next(it), next(it)
            adj[a].append((c, b)); adj[b].append((c, a))
            total += c
        # Prim 求最大生成樹（圖保證連通）
        seen = [False] * (n + 1)
        heap = [(0, 1)]
        kept = 0
        while heap:
            c, u = heapq.heappop(heap)
            if seen[u]:
                continue
            seen[u] = True
            kept += -c
            for w, v in adj[u]:
                if not seen[v]:
                    heapq.heappush(heap, (-w, v))
        res.append(str(total - kept))
    return "\n".join(res) + "\n"
