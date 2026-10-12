"""UVa 446 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.splitlines()
    res = []
    for line in lines[1:1 + int(lines[0])]:
        a, op, b = line.split()
        x, y = int(a, 16), int(b, 16)
        r = x + y if op == "+" else x - y
        res.append(f"{x:013b} {op} {y:013b} = {r}")
    return "\n".join(res) + "\n"
