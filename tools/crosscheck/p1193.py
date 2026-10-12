"""UVa 1193 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import math

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    p, cs, res = 0, 0, []
    while True:
        n, d = v[p], v[p + 1]; p += 2
        if n == 0 and d == 0:
            break
        pts = [(v[p + 2 * i], v[p + 2 * i + 1]) for i in range(n)]
        p += 2 * n
        cs += 1
        if any(abs(y) > d for _, y in pts):
            res.append(f"Case {cs}: -1")
            continue
        # 每個島對應海岸上的一段區間；依左端排序，維護目前雷達能放的最右位置
        iv = sorted((x - math.sqrt(d * d - y * y), x + math.sqrt(d * d - y * y)) for x, y in pts)
        count, reach = 0, None
        for lo, hi in iv:
            if reach is None or lo > reach:
                count += 1
                reach = hi
            else:
                reach = min(reach, hi)
        res.append(f"Case {cs}: {count}")
    return "\n".join(res) + "\n"
