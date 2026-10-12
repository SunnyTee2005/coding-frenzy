"""UVa 11934 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(0, len(v), 5):
        a, b, c, d, l = v[i:i + 5]
        if a == b == c == d == l == 0:
            break
        res.append(str(sum(1 for x in range(l + 1) if (a * x * x + b * x + c) % d == 0)))
    return "\n".join(res) + "\n"
