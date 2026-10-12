"""UVa 993 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    res = []
    for n in t[1:1 + t[0]]:
        if n < 10:
            res.append(str(10 if n == 0 else n)); continue
        digits = []
        for f in range(9, 1, -1):
            while n % f == 0:
                digits.append(f); n //= f
        res.append("-1" if n != 1 else "".join(map(str, sorted(digits))))
    return "\n".join(res) + "\n"
