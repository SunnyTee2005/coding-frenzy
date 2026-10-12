"""UVa 10268 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    res = []
    for xl, al in zip(lines[0::2], lines[1::2]):
        if not xl.strip():
            break
        x, a = int(xl), list(map(int, al.split()))
        n = len(a) - 1
        res.append(str(sum(a[i] * (n - i) * x ** (n - i - 1) for i in range(n))))
    return "\n".join(res) + "\n"
