"""UVa 11309 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    res = []
    for hm in t[1:1 + int(t[0])]:
        h, m = map(int, hm.split(":"))
        cur = h * 60 + m
        while True:
            cur = (cur + 1) % 1440
            digits = f"{cur // 60:02d}{cur % 60:02d}".lstrip("0") or "0"
            if digits == digits[::-1]:
                break
        res.append(f"{cur // 60:02d}:{cur % 60:02d}")
    return "\n".join(res) + "\n"
