"""UVa 1237 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    p, blocks = 1, []
    for _ in range(int(tok[0])):
        d = int(tok[p]); p += 1
        db = [(tok[p + 3 * i], int(tok[p + 3 * i + 1]), int(tok[p + 3 * i + 2])) for i in range(d)]
        p += 3 * d
        q = int(tok[p]); p += 1
        lines = []
        for x in map(int, tok[p:p + q]):
            hits = [n for n, l, h in db if l <= x <= h]
            lines.append(hits[0] if len(hits) == 1 else "UNDETERMINED")
        p += q
        blocks.append("".join(l + "\n" for l in lines))
    return "\n".join(blocks)
