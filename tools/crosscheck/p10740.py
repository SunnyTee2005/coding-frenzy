"""UVa 10740 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import heapq

def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    while True:
        n, m = next(it), next(it)
        if n == 0 and m == 0:
            break
        x, y, k = next(it), next(it), next(it)
        adj = {}
        for _ in range(m):
            u, v, l = next(it), next(it), next(it)
            adj.setdefault(u, []).append((v, l))
        # 第 k 短的路徑長度：每個點最多出堆 k 次
        popped = {}
        lengths = []
        heap = [(0, x)]
        while heap and len(lengths) < k:
            d, u = heapq.heappop(heap)
            if popped.get(u, 0) >= k:
                continue
            popped[u] = popped.get(u, 0) + 1
            if u == y:
                lengths.append(d)
            for v, l in adj.get(u, []):
                heapq.heappush(heap, (d + l, v))
        res.append(str(lengths[k - 1]) if len(lengths) >= k else "-1")
    return "\n".join(res) + "\n"
