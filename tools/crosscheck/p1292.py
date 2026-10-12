"""UVa 1292 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import re
import sys
from itertools import combinations

def solve(s: str) -> str:
    sys.setrecursionlimit(10000)
    lines = s.split("\n")
    p, res = 0, []
    while p < len(lines) and lines[p].strip():
        n = int(lines[p]); p += 1
        edges = []
        for _ in range(n):
            nums = list(map(int, re.findall(r"\d+", lines[p]))); p += 1
            edges += [(nums[0], c) for c in nums[2:]]
        if n <= 12:  # 小的直接枚舉最少點覆蓋
            best = next(r for r in range(n + 1) for pick in combinations(range(n), r)
                        if all(a in pick or b in pick for a, b in edges))
            res.append(str(best))
            continue
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b); adj[b].append(a)
        # 貪心：從葉子往上，葉子的父親一定放士兵
        order, parent, seen = [], {0: None}, {0}
        stack = [0]
        while stack:
            u = stack.pop(); order.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); parent[v] = u; stack.append(v)
        covered, chosen = set(), set()
        for u in reversed(order):
            pu = parent[u]
            if pu is not None and u not in chosen and (u, pu) not in covered:
                chosen.add(pu)
                for v in adj[pu]:
                    covered.add((v, pu)); covered.add((pu, v))
        res.append(str(len(chosen)))
    return "\n".join(res) + "\n"
