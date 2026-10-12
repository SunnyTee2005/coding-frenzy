"""UVa 573 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(0, len(v), 4):
        H, U, D, F = v[i:i + 4]
        if H == 0:
            break
        # 全部乘以 100 用整數算，避免浮點誤差：爬升量 = 100U - (day-1)*U*F
        h, day = 0, 0
        while True:
            day += 1
            climb = 100 * U - (day - 1) * U * F
            h += max(climb, 0)
            if h > 100 * H:
                res.append(f"success on day {day}")
                break
            h -= 100 * D
            if h < 0:
                res.append(f"failure on day {day}")
                break
    return "\n".join(res) + "\n"
