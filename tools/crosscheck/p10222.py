"""UVa 10222 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


ROWS = ["`1234567890-=", "qwertyuiop[]\\", "asdfghjkl;'", "zxcvbnm,./"]
DEC = {row[i + 2]: row[i] for row in ROWS for i in range(len(row) - 2)}

def solve(s: str) -> str:
    lines = s.split("\n")
    n = int(lines[0])
    return "".join("".join(DEC.get(c.lower(), c) for c in line) + "\n" for line in lines[1:1 + n])
