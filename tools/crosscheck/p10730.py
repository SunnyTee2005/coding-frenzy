"""UVa 10730 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for line in s.splitlines():
        if line.strip() == "0":
            break
        head, rest = line.split(":")
        p = list(map(int, rest.split()))
        pos = {v: i for i, v in enumerate(p)}
        bad = any(pos.get(2 * p[j] - p[i], -1) > j for i in range(len(p)) for j in range(i + 1, len(p)))
        res.append("no" if bad else "yes")
    return "\n".join(res) + "\n"
