"""UVa 11764 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for c in range(1, next(it) + 1):
        h = [next(it) for _ in range(next(it))]
        res.append(f"Case {c}: {sum(b > a for a, b in zip(h, h[1:]))} {sum(b < a for a, b in zip(h, h[1:]))}")
    return "\n".join(res) + "\n"
