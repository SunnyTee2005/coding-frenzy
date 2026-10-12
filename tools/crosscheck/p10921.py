"""UVa 10921 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    table = {}
    for digit, letters in zip("23456789", ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]):
        for ch in letters:
            table[ch] = digit
    res = []
    for line in s.splitlines():
        if not line:
            continue
        res.append(f"{''.join(table.get(c, c) for c in line)} {sum(c.isupper() for c in line)} {line.count('-')}")
    return "\n".join(res) + "\n"
