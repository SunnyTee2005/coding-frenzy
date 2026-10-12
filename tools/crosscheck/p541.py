"""UVa 541 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for n in it:
        if n == 0:
            break
        m = [[next(it) for _ in range(n)] for _ in range(n)]
        rows = [i for i in range(n) if sum(m[i]) % 2]
        cols = [j for j in range(n) if sum(r[j] for r in m) % 2]
        if not rows and not cols:
            res.append("OK")
        elif len(rows) == 1 and len(cols) == 1:
            res.append(f"Change bit ({rows[0] + 1},{cols[0] + 1})")
        else:
            res.append("Corrupt")
    return "\n".join(res) + "\n"
