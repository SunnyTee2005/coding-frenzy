"""UVa 10055 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    return ''.join(f'{abs(int(a) - int(b))}\n' for a, b in (l.split() for l in s.splitlines() if l.strip()))
