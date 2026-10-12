"""UVa 118 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    mx, my = int(tok[0]), int(tok[1])
    move = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    order = "NESW"
    scent, res = set(), []
    for i in range(2, len(tok), 4):
        x, y, o, cmd = int(tok[i]), int(tok[i + 1]), tok[i + 2], tok[i + 3]
        lost = False
        for c in cmd:
            if c in "LR":
                o = order[(order.index(o) + (1 if c == "R" else -1)) % 4]
                continue
            nx, ny = x + move[o][0], y + move[o][1]
            if 0 <= nx <= mx and 0 <= ny <= my:
                x, y = nx, ny
            elif (x, y) not in scent:
                scent.add((x, y))
                lost = True
                break
        res.append(f"{x} {y} {o}" + (" LOST" if lost else ""))
    return "\n".join(res) + "\n"
