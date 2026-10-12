"""UVa 11455 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(v[0]):
        a, b, c, d = sorted(v[1 + 4 * i:5 + 4 * i])
        if a == d:
            res.append("square")
        elif a == b and c == d:
            res.append("rectangle")
        elif d < a + b + c:
            res.append("quadrangle")
        else:
            res.append("banana")
    return "\n".join(res) + "\n"
