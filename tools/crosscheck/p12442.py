"""UVa 12442 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for cs in range(1, next(it) + 1):
        n = next(it)
        nxt = [0] * (n + 1)
        for _ in range(n):
            u, v = next(it), next(it)
            nxt[u] = v
        # 反覆求：每個人能看到的人數 = 從他出發走到重複為止的不同人數（記憶化）
        memo = [0] * (n + 1)
        for s0 in range(1, n + 1):
            if memo[s0]:
                continue
            order, pos = [], {}
            u = s0
            while not memo[u] and u not in pos:
                pos[u] = len(order); order.append(u); u = nxt[u]
            if memo[u]:
                base = memo[u]
                for w in reversed(order):
                    base += 1; memo[w] = base
            else:
                start = pos[u]
                cyc = len(order) - start
                for w in order[start:]:
                    memo[w] = cyc
                base = cyc
                for w in reversed(order[:start]):
                    base += 1; memo[w] = base
        best = max(range(1, n + 1), key=lambda i: (memo[i], -i))
        res.append(f"Case {cs}: {best}")
    return "\n".join(res) + "\n"
