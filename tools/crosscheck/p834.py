"""UVa 834 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from fractions import Fraction

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for a, b in zip(v[0::2], v[1::2]):
        x = Fraction(a, b)
        terms = []
        while True:
            t = x.numerator // x.denominator
            terms.append(t)
            x -= t
            if x == 0:
                break
            x = 1 / x
        res.append(f"[{terms[0]};" + ",".join(map(str, terms[1:])) + "]")
    return "\n".join(res) + "\n"
