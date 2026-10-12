"""UVa 12468 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    res = []
    for a, b in zip(t[::2], t[1::2]):
        if a == -1 and b == -1:
            break
        res.append(str(min((a - b) % 100, (b - a) % 100)))
    return "\n".join(res) + "\n"
