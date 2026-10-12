"""UVa 10150 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import deque

def solve(s: str) -> str:
    dict_part, _, query_part = s.partition("\n\n")
    words = set(dict_part.split("\n"))
    by_len = {}
    for w in words:
        by_len.setdefault(len(w), []).append(w)
    blocks = []
    for line in query_part.split("\n"):
        if not line.strip():
            continue
        a, b = line.split()
        if a not in words or b not in words:
            blocks.append("No solution.\n")
            continue
        prev = {a: None}
        q = deque([a])
        while q:
            u = q.popleft()
            for v in by_len[len(u)]:
                if v not in prev and sum(x != y for x, y in zip(u, v)) == 1:
                    prev[v] = u
                    q.append(v)
        if b not in prev:
            blocks.append("No solution.\n")
            continue
        path = []
        while b is not None:
            path.append(b)
            b = prev[b]
        blocks.append("".join(w + "\n" for w in reversed(path)))
    return "\n".join(blocks)
