"""UVa 11498 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for k in it:
        if k == 0:
            break
        n, m = next(it), next(it)
        for _ in range(k):
            x, y = next(it), next(it)
            if x == n or y == m:
                res.append("divisa")
            else:
                res.append(("N" if y > m else "S") + ("E" if x > n else "O"))
    return "\n".join(res) + "\n"
