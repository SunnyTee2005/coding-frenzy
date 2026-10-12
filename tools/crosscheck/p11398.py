"""UVa 11398 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res, bits, flag = [], "", "1"
    for tok in s.split():
        if tok == "~":
            break
        if tok == "#":
            res.append(str(int(bits, 2) if bits else 0)); bits, flag = "", "1"
        elif tok == "0":
            flag = "1"
        elif tok == "00":
            flag = "0"
        else:
            bits += flag * (len(tok) - 2)
    return "\n".join(res) + "\n"
