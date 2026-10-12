"""UVa 458 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    return "".join(c if c == "\n" else chr(ord(c) - 7) for c in s)
