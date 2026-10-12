"""UVa 145 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


RATES = {"A": (10, 6, 2), "B": (25, 15, 5), "C": (53, 33, 13), "D": (87, 47, 17), "E": (144, 80, 30)}

def period(minute):
    h = minute // 60
    return 0 if 8 <= h < 18 else (1 if 18 <= h < 22 else 2)

def solve(s: str) -> str:
    res = []
    for line in s.split("\n"):
        if line.startswith("#"):
            break
        step, num, h1, m1, h2, m2 = line.split()
        start, end = int(h1) * 60 + int(m1), int(h2) * 60 + int(m2)
        length = (end - start) % 1440 or 1440
        mins = [0, 0, 0]
        for i in range(length):
            mins[period((start + i) % 1440)] += 1
        cents = sum(m * r for m, r in zip(mins, RATES[step]))
        cost = f"{cents // 100}.{cents % 100:02d}"
        res.append(f"{num:>10}{mins[0]:>6}{mins[1]:>6}{mins[2]:>6}{step:>3}{cost:>8}")
    return "".join(r + "\n" for r in res)
