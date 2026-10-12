"""UVa 11956 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    res = []
    for c, p in enumerate(t[1:1 + int(t[0])], 1):
        mem, ptr = [0] * 100, 0
        for ch in p:
            if ch == ">":
                ptr = (ptr + 1) % 100
            elif ch == "<":
                ptr = (ptr - 1) % 100
            elif ch == "+":
                mem[ptr] = (mem[ptr] + 1) % 256
            elif ch == "-":
                mem[ptr] = (mem[ptr] - 1) % 256
        res.append(f"Case {c}: " + " ".join(f"{v:02X}" for v in mem))
    return "\n".join(res) + "\n"
