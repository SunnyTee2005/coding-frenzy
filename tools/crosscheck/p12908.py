"""UVa 12908 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from math import isqrt

def solve(s: str) -> str:
    res = []
    for x in map(int, s.split()):
        if x == 0:
            break
        n = (isqrt(8 * x + 1) - 1) // 2  # 最大的 n 使 n(n+1)/2 <= x
        n += 1
        res.append(f"{n * (n + 1) // 2 - x} {n}")
    return "\n".join(res) + "\n"
