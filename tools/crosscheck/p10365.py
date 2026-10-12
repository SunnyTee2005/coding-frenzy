"""UVa 10365 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    res = []
    for n in t[1:1 + t[0]]:
        best = min(2 * (a * b + b * c + a * c) for a in range(1, n + 1) if n % a == 0
                   for b in range(1, n // a + 1) if (n // a) % b == 0 for c in [n // a // b])
        res.append(str(best))
    return "\n".join(res) + "\n"
