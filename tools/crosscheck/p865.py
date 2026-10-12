"""UVa 865 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    t, p, blocks = int(lines[0]), 2, []
    for _ in range(t):
        plain, sub = lines[p], lines[p + 1]
        p += 2
        table = str.maketrans(plain, sub)
        out = [sub, plain]
        while p < len(lines) and lines[p] != "":
            out.append(lines[p].translate(table))
            p += 1
        p += 1
        blocks.append("".join(o + "\n" for o in out))
    return "\n".join(blocks)
