"""UVa 11677 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(0, len(v), 4):
        h1, m1, h2, m2 = v[i:i + 4]
        if h1 == m1 == h2 == m2 == 0:
            break
        res.append(str(((h2 - h1) * 60 + m2 - m1) % 1440))
    return "\n".join(res) + "\n"
