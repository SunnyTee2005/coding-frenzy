"""UVa 12959 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    while True:
        j, r = next(it), next(it)
        if j == 0 and r == 0:
            break
        v = [next(it) for _ in range(j * r)]
        tot = [sum(v[i::j]) for i in range(j)]
        best = max(tot)
        res.append(str(max(i for i in range(j) if tot[i] == best) + 1))
    return "\n".join(res) + "\n"
