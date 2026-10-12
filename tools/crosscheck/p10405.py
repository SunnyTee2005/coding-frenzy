"""UVa 10405 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")[:-1]
    res = []
    for a, b in zip(lines[0::2], lines[1::2]):
        prev = [0] * (len(b) + 1)
        for ch in a:
            cur = [0]
            for j, cb in enumerate(b):
                cur.append(prev[j] + 1 if ch == cb else max(prev[j + 1], cur[j]))
            prev = cur
        res.append(str(prev[-1]))
    return "".join(r + "\n" for r in res)
