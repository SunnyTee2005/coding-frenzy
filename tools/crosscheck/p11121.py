"""UVa 11121 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    res = []
    for i, n in enumerate(t[1:1 + t[0]], 1):
        digits = ""
        if n == 0:
            digits = "0"
        while n:
            n, r = divmod(n, -2)
            if r:
                n += 1
            digits = str(abs(r)) + digits
        res.append(f"Case #{i}: {digits}")
    return "\n".join(res) + "\n"
