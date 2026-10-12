"""UVa 11518 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import deque

def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        n, m, l = next(it), next(it), next(it)
        adj = {}
        for _ in range(m):
            x, y = next(it), next(it)
            adj.setdefault(x, []).append(y)
        fallen = set()
        for _ in range(l):
            q = deque([next(it)])
            while q:
                u = q.popleft()
                if u in fallen:
                    continue
                fallen.add(u)
                q.extend(adj.get(u, []))
        res.append(str(len(fallen)))
    return "\n".join(res) + "\n"
