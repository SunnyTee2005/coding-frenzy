"""UVa 12195 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from fractions import Fraction

DUR = {"W": Fraction(1), "H": Fraction(1, 2), "Q": Fraction(1, 4), "E": Fraction(1, 8),
       "S": Fraction(1, 16), "T": Fraction(1, 32), "X": Fraction(1, 64)}

def solve(s: str) -> str:
    res = []
    for line in s.split():
        if line == "*":
            break
        measures = line.strip("/").split("/")
        res.append(str(sum(1 for m in measures if sum(DUR[c] for c in m) == 1)))
    return "\n".join(res) + "\n"
