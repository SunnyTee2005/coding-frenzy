"""UVa 11321 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import math

def cmod(a, m):
    return int(math.fmod(a, m))  # C 語言規則：餘數與被除數同號

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    p, res = 0, []
    while True:
        n, m = v[p], v[p + 1]
        res.append(f"{n} {m}")
        if n == 0 and m == 0:
            break
        nums = v[p + 2:p + 2 + n]
        p += 2 + n
        nums.sort(key=lambda x: (cmod(x, m), 0 if x % 2 else 1, -x if x % 2 else x))
        res += map(str, nums)
    return "\n".join(res) + "\n"
