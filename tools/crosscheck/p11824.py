"""UVa 11824 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        v = []
        for x in it:
            if x == 0:
                break
            v.append(x)
        v.sort(reverse=True)
        total = sum(2 * x ** (i + 1) for i, x in enumerate(v))
        res.append("Too expensive" if total > 5000000 else str(total))
    return "\n".join(res) + "\n"
