"""UVa 516 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for line in s.splitlines():
        t = list(map(int, line.split()))
        if t == [0]:
            break
        x = 1
        for p, e in zip(t[::2], t[1::2]):
            x *= p ** e
        x -= 1
        f, d = [], 2
        while d * d <= x:
            c = 0
            while x % d == 0:
                x //= d; c += 1
            if c:
                f.append((d, c))
            d += 1
        if x > 1:
            f.append((x, 1))
        res.append(" ".join(f"{p} {e}" for p, e in reversed(f)))
    return "\n".join(res) + "\n"
