"""UVa 10056 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    res = []
    for k in range(int(tok[0])):
        n, p, i = int(tok[1 + 3 * k]), float(tok[2 + 3 * k]), int(tok[3 + 3 * k])
        q = 1 - p
        res.append(f"{p * q ** (i - 1) / (1 - q ** n):.4f}")
    return "\n".join(res) + "\n"
