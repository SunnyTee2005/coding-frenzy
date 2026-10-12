"""UVa 11063 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res, cs = [], 0
    for n in it:
        b = [next(it) for _ in range(n)]
        cs += 1
        ok = b[0] >= 1 and all(x < y for x, y in zip(b, b[1:]))
        if ok:
            sums = [b[i] + b[j] for i in range(n) for j in range(i, n)]
            ok = len(set(sums)) == len(sums)
        res.append(f"Case #{cs}: It is {'' if ok else 'not '}a B2-Sequence.\n")
    return "\n".join(res) + "\n" if res else ""
