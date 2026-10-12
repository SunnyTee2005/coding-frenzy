"""UVa 12592 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    n = int(lines[0])
    m = {lines[1 + 2 * i]: lines[2 + 2 * i] for i in range(n)}
    q = int(lines[1 + 2 * n])
    return "".join(m[x] + "\n" for x in lines[2 + 2 * n:2 + 2 * n + q])
