"""UVa 272 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    out, o = [], True
    for ch in s:
        if ch == '"':
            out.append('``' if o else "''"); o = not o
        else:
            out.append(ch)
    return ''.join(out)
