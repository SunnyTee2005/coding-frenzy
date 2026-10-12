"""UVa 12970 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from fractions import Fraction

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(0, len(v), 4):
        v1, d1, v2, d2 = v[i:i + 4]
        if v1 == d1 == v2 == d2 == 0:
            break
        t1, t2 = Fraction(d1, v1), Fraction(d2, v2)
        res.append(f"Case #{i // 4 + 1}: " + ("You owe me a beer!" if t1 < t2 else "No beer for the captain."))
        avg = (t1 + t2) / 2
        res.append("Avg. arrival time: " + (str(avg.numerator) if avg.denominator == 1 else f"{avg.numerator}/{avg.denominator}"))
    return "\n".join(res) + "\n"
