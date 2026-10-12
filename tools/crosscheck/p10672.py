"""UVa 10672 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    p, res = 0, []
    while True:
        n = int(lines[p]); p += 1
        if n == 0:
            break
        parent, marbles, children = {}, {}, {}
        for _ in range(n):
            nums = list(map(int, lines[p].split())); p += 1
            v, m, d = nums[0], nums[1], nums[2]
            marbles[v] = m
            children[v] = nums[3:3 + d]
            for c in children[v]:
                parent[c] = v
        root = next(v for v in marbles if v not in parent)
        # 由下往上：每條邊的流量 = 子樹彈珠數 - 子樹節點數
        order, stack = [], [root]
        while stack:
            u = stack.pop(); order.append(u); stack.extend(children[u])
        size = {v: 1 for v in marbles}
        total = dict(marbles)
        moves = 0
        for u in reversed(order):
            if u != root:
                moves += abs(total[u] - size[u])
                size[parent[u]] += size[u]
                total[parent[u]] += total[u]
        res.append(str(moves))
    return "\n".join(res) + "\n"
