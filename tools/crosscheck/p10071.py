"""UVa 10071 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    return "".join(f"{2 * a * b}\n" for a, b in zip(v[0::2], v[1::2]))
