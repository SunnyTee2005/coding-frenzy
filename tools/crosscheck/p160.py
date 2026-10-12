"""UVa 160 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        counts = []
        for p in range(2, n + 1):
            if all(p % d for d in range(2, p)):
                c, m = 0, n
                # 直接數 1..n 每個數含幾個因數 p
                for x in range(2, n + 1):
                    while x % p == 0:
                        x //= p; c += 1
                counts.append(c)
        cells = [f"{c:3d}" for c in counts]
        lines = ["".join(cells[i:i + 15]) for i in range(0, len(cells), 15)]
        res.append(f"{n:3d}! =" + "\n      ".join(lines))
    return "".join(r + "\n" for r in res)
