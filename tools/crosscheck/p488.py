"""UVa 488 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    cases = []
    for i in range(v[0]):
        a, f = v[1 + 2 * i], v[2 + 2 * i]
        heights = list(range(1, a + 1)) + list(range(a - 1, 0, -1))
        wave = "".join(str(h) * h + "\n" for h in heights)
        cases.append("\n".join([wave] * f))
    return "\n".join(cases)
