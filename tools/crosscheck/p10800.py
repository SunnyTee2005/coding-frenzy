"""UVa 10800 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    out = []
    for no, w in enumerate(t[1:1 + int(t[0])], 1):
        cells, h = {}, 0
        for i, ch in enumerate(w):
            if ch == "R":
                cells[(h, i)] = "/"; h += 1
            elif ch == "F":
                h -= 1; cells[(h, i)] = "\\"
            else:
                cells[(h, i)] = "_"
        levels = sorted({lv for lv, _ in cells}, reverse=True)
        out.append(f"Case #{no}:")
        for lv in levels:
            line = "".join(cells.get((lv, i), " ") for i in range(len(w))).rstrip()
            out.append("| " + line)
        out.append("+" + "-" * (len(w) + 2))
        out.append("")
    return "\n".join(out) + "\n"
