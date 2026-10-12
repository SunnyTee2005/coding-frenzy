"""UVa 12820 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    t = s.split()
    i, c, res = 0, 0, []
    while i < len(t):
        n = int(t[i]); words = t[i + 1:i + 1 + n]; i += 1 + n
        c += 1
        cool = 0
        for w in words:
            counts = list(Counter(w).values())
            cool += len(counts) >= 2 and len(set(counts)) == len(counts)
        res.append(f"Case {c}: {cool}")
    return "\n".join(res) + "\n"
