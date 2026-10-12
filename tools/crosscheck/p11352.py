"""UVa 11352 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import deque

def solve(s: str) -> str:
    t = s.split()
    i, res = 1, []
    for _ in range(int(t[0])):
        m, n = int(t[i]), int(t[i + 1]); i += 2
        g = t[i:i + m]; i += m
        blocked = set()
        for r in range(m):
            for c in range(n):
                if g[r][c] == "Z":
                    blocked.add((r, c))
                    for dr, dc in [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]:
                        a, b = r + dr, c + dc
                        if 0 <= a < m and 0 <= b < n and g[a][b] not in "AB":
                            blocked.add((a, b))
        start = next((r, c) for r in range(m) for c in range(n) if g[r][c] == "A")
        seen = {start: 0}
        dq = deque([start])
        ans = None
        while dq:
            r, c = dq.popleft()
            if g[r][c] == "B":
                ans = seen[(r, c)]; break
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    a, b = r + dr, c + dc
                    if (dr or dc) and 0 <= a < m and 0 <= b < n and (a, b) not in blocked and (a, b) not in seen:
                        seen[(a, b)] = seen[(r, c)] + 1; dq.append((a, b))
        res.append("King Peter, you can't go now!" if ans is None else f"Minimal possible length of a trip is {ans}")
    return "\n".join(res) + "\n"
