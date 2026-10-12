"""UVa 10943 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from math import comb

def solve(s: str) -> str:
    t = list(map(int, s.split()))
    res = []
    for n, k in zip(t[::2], t[1::2]):
        if n == 0 and k == 0:
            break
        res.append(str(comb(n + k - 1, k - 1) % 1000000))
    return "\n".join(res) + "\n"
