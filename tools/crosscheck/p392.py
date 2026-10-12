"""UVa 392 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    res = []
    for i in range(0, len(t), 9):
        terms = []
        for j, v in enumerate(t[i:i + 9]):
            deg = 8 - j
            if v == 0:
                continue
            mag = abs(v)
            body = ("" if mag == 1 and deg > 0 else str(mag)) + ("x" if deg > 0 else "") + (f"^{deg}" if deg > 1 else "")
            terms.append((v < 0, body))
        if not terms:
            res.append("0"); continue
        line = ("-" if terms[0][0] else "") + terms[0][1]
        for neg, body in terms[1:]:
            line += (" - " if neg else " + ") + body
        res.append(line)
    return "\n".join(res) + "\n"
