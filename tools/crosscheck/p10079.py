"""UVa 10079 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n < 0:
            break
        res.append(str(1 + sum(range(1, n + 1)) if n < 1000 else n * (n + 1) // 2 + 1))
    return "\n".join(res) + "\n"
