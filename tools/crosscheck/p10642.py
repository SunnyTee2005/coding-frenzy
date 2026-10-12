"""UVa 10642 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    def pos(x, y):
        # 第 d 條對角線（x+y=d）之前共有 1+2+...+d 個圓
        return sum(range(x + y + 1)) + x
    for i in range(v[0]):
        a, b, x, y = v[1 + 4 * i:5 + 4 * i]
        res.append(f"Case {i + 1}: {pos(x, y) - pos(a, b)}")
    return "\n".join(res) + "\n"
