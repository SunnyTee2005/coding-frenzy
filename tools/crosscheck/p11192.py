"""UVa 11192 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    res = []
    for i in range(0, len(tok), 2):
        if tok[i] == "0":
            break
        g, w = int(tok[i]), tok[i + 1]
        n = len(w) // g
        res.append("".join(w[j:j + n][::-1] for j in range(0, len(w), n)))
    return "\n".join(res) + "\n"
