"""UVa 389 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


D = "0123456789ABCDEF"

def solve(s: str) -> str:
    res = []
    for line in s.split("\n"):
        if not line.strip():
            continue
        num, a, b = line.split()
        v, b = int(num, int(a)), int(b)
        r = ""
        while True:
            r = D[v % b] + r
            v //= b
            if v == 0:
                break
        res.append(r[-7:].rjust(7, "0"))
    return "\n".join(res) + "\n"
