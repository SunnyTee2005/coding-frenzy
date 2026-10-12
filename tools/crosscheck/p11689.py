"""UVa 11689 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(v[0]):
        e, f, c = v[1 + 3 * i:4 + 3 * i]
        empty, drunk = e + f, 0
        while empty >= c:  # 一次換一瓶
            empty -= c - 1
            drunk += 1
        res.append(str(drunk))
    return "\n".join(res) + "\n"
