"""UVa 12650 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    p, res = 0, []
    while p < len(v):
        n, r = v[p], v[p + 1]
        back = set(v[p + 2:p + 2 + r])
        p += 2 + r
        miss = [i for i in range(1, n + 1) if i not in back]
        res.append("".join(f"{i} " for i in miss) if miss else "*")
    return "\n".join(res) + "\n"
