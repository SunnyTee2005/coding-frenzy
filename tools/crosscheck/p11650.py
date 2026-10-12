"""UVa 11650 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    res = []
    for hm in t[1:1 + int(t[0])]:
        h, m = map(int, hm.split(":"))
        minutes = (12 * 60 - (h % 12) * 60 - m) % (12 * 60)
        h2, m2 = divmod(minutes, 60)
        res.append(f"{h2 or 12:02d}:{m2:02d}")
    return "\n".join(res) + "\n"
