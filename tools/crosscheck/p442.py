"""UVa 442 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    n = int(lines[0])
    dims = {}
    for line in lines[1:1 + n]:
        nm, r, c = line.split()
        dims[nm] = (int(r), int(c))
    res = []
    for e in lines[1 + n:]:
        if not e.strip():
            continue
        # 遞迴下降解析：回傳 (列, 行, 乘法次數)，維度不合時丟出例外
        pos = 0
        def parse():
            nonlocal pos
            if e[pos] == "(":
                pos += 1
                r1, c1, x = parse()
                r2, c2, y = parse()
                pos += 1  # ')'
                if c1 != r2:
                    raise ValueError
                return r1, c2, x + y + r1 * c1 * c2
            nm = e[pos]; pos += 1
            return dims[nm][0], dims[nm][1], 0
        try:
            res.append(str(parse()[2]))
        except ValueError:
            res.append("error")
    return "\n".join(res) + "\n"
