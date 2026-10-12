"""UVa 417 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from math import comb

def index(w):
    if any(a >= b for a, b in zip(w, w[1:])):
        return 0
    n = len(w)
    total = sum(comb(26, l) for l in range(1, n))  # 較短的字
    prev = -1
    for i, ch in enumerate(w):
        c = ord(ch) - 97
        # 這一位比 ch 小（且大於前一位）的字母，後面剩 n-i-1 位任選
        for smaller in range(prev + 1, c):
            total += comb(25 - smaller, n - i - 1)
        prev = c
    return total + 1

def solve(s: str) -> str:
    return "".join(f"{index(w)}\n" for w in s.split())
