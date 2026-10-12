"""UVa 11000 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    fib = [0, 1]
    while len(fib) < 60:
        fib.append(fib[-1] + fib[-2])
    res = []
    for n in map(int, s.split()):
        if n < 0:
            break
        # 公蜂數 = F(n+2) - 1，總數 = F(n+3) - 1（F 為費氏數列）
        res.append(f"{fib[n + 2] - 1} {fib[n + 3] - 1}")
    return "\n".join(res) + "\n"
