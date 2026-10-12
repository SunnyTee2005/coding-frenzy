"""UVa 10699 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        x, ps, d = n, set(), 2
        while d * d <= x:
            while x % d == 0:
                ps.add(d); x //= d
            d += 1
        if x > 1:
            ps.add(x)
        res.append(f"{n} : {len(ps)}")
    return "\n".join(res) + "\n"
