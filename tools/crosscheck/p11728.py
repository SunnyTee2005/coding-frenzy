"""UVa 11728 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    sigma = {}
    for x in range(1, 1001):
        total = sum(d for d in range(1, x + 1) if x % d == 0)
        sigma.setdefault(total, []).append(x)
    res = []
    for i, v in enumerate(map(int, s.split()), 1):
        if v == 0:
            break
        res.append(f"Case {i}: {max(sigma.get(v, [-1]))}")
    return "\n".join(res) + "\n"
