"""UVa 10789 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    lines = s.split()
    res = []
    for i, w in enumerate(lines[1:1 + int(lines[0])]):
        c = Counter(w)
        ok = sorted(ch for ch, v in c.items() if v > 1 and all(v % d for d in range(2, int(v ** 0.5) + 1)))
        res.append(f"Case {i + 1}: {''.join(ok) or 'empty'}")
    return "\n".join(res) + "\n"
