"""UVa 10931 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        b = bin(n)[2:]
        res.append(f"The parity of {b} is {b.count('1')} (mod 2).")
    return "\n".join(res) + "\n"
