"""UVa 12015 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    res = []
    for c in range(int(tok[0])):
        rows = [(tok[1 + 20 * c + 2 * i], int(tok[2 + 20 * c + 2 * i])) for i in range(10)]
        best = max(v for _, v in rows)
        res.append(f"Case #{c + 1}:")
        res += [u for u, v in rows if v == best]
    return "\n".join(res) + "\n"
