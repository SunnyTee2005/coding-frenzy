"""UVa 10082 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


ROWS = ["`1234567890-=", "QWERTYUIOP[]\\", "ASDFGHJKL;'", "ZXCVBNM,./"]
DEC = {r[i + 1]: r[i] for r in ROWS for i in range(len(r) - 1)}

def solve(s: str) -> str:
    return "".join(DEC.get(ch, ch) for ch in s)
