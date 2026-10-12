"""UVa 13178 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    # 1..n 串起來的數字和 ≡ n(n+1)/2 (mod 3)
    return "".join(("YES" if (n * (n + 1) // 2) % 3 == 0 else "NO") + "\n" for n in t[1:1 + t[0]])
