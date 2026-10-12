"""UVa 1339 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    w = s.split()
    res = []
    for a, b in zip(w[0::2], w[1::2]):
        res.append("YES" if sorted(Counter(a).values()) == sorted(Counter(b).values()) else "NO")
    return "\n".join(res) + "\n"
