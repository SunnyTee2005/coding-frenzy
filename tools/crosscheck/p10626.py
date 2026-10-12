"""UVa 10626 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from functools import lru_cache

# 每買一瓶可投入的硬幣組合：拿掉任何一枚就不夠 8 元（多投沒有好處）
PAYS = []
for a in range(3):
    for b in range(3):
        for c in range(9):
            paid = 10 * a + 5 * b + c
            if paid < 8:
                continue
            if any(paid - v >= 8 for v, cnt in ((10, a), (5, b), (1, c)) if cnt):
                continue
            ch = paid - 8
            PAYS.append((a, b, c, ch // 10, ch % 10 // 5, ch % 5))

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(v[0]):
        cokes, n1, n5, n10 = v[1 + 4 * i:5 + 4 * i]

        @lru_cache(maxsize=None)
        def best(left, n1, n5, n10):
            if left == 0:
                return 0
            r = float("inf")
            for a, b, c, g10, g5, g1 in PAYS:
                if a <= n10 and b <= n5 and c <= n1:
                    r = min(r, a + b + c + best(left - 1, n1 - c + g1, n5 - b + g5, n10 - a + g10))
            return r
        res.append(str(best(cokes, n1, n5, n10)))
    return "\n".join(res) + "\n"
