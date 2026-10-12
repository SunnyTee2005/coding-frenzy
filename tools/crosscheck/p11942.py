"""UVa 11942 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    n = t[0]
    res = ["Lumberjacks:"]
    for g in range(n):
        v = t[1 + 10 * g: 11 + 10 * g]
        res.append("Ordered" if v == sorted(v) or v == sorted(v, reverse=True) else "Unordered")
    return "\n".join(res) + "\n"
