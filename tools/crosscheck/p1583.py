"""UVa 1583 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for n in v[1:1 + v[0]]:
        ans = 0
        for g in range(max(1, n - 54), n):
            if g + sum(map(int, str(g))) == n:
                ans = g
                break
        res.append(str(ans))
    return "\n".join(res) + "\n"
