"""UVa 11369 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    i, res = 1, []
    for _ in range(t[0]):
        n = t[i]; p = sorted(t[i + 1:i + 1 + n], reverse=True); i += 1 + n
        res.append(str(sum(p[2::3])))
    return "\n".join(res) + "\n"
