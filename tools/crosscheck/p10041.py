"""UVa 10041 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        r = next(it)
        v = [next(it) for _ in range(r)]
        res.append(str(min(sum(abs(x - h) for x in v) for h in set(v))))
    return "\n".join(res) + "\n"
