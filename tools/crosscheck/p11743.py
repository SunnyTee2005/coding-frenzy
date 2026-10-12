"""UVa 11743 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.splitlines()
    res = []
    for line in lines[1:1 + int(lines[0])]:
        digits = [int(c) for c in line if c.isdigit()]
        total = 0
        # 從倒數第二位開始往前，每隔一位加倍
        for i, x in enumerate(reversed(digits)):
            if i % 2 == 1:
                total += sum(map(int, str(2 * x)))
            else:
                total += x
        res.append("Valid" if total % 10 == 0 else "Invalid")
    return "\n".join(res) + "\n"
