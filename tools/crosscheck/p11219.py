"""UVa 11219 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    res = []
    for i in range(int(t[0])):
        cd, cm, cy = map(int, t[1 + 2 * i].split("/"))
        bd, bm, by = map(int, t[2 + 2 * i].split("/"))
        age = cy - by - (1 if (cm, cd) < (bm, bd) else 0)
        if (by, bm, bd) > (cy, cm, cd):
            ans = "Invalid birth date"
        elif age > 130:
            ans = "Check birth date"
        else:
            ans = str(age)
        res.append(f"Case #{i + 1}: {ans}")
    return "\n".join(res) + "\n"
