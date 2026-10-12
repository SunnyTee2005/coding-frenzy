"""UVa 10550 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(0, len(v), 4):
        pos, a, b, c = v[i:i + 4]
        if pos == a == b == c == 0:
            break
        deg = 720
        cw = lambda x, y: (x - y) % 40   # 順時針：數字遞減
        ccw = lambda x, y: (y - x) % 40  # 逆時針：數字遞增
        deg += cw(pos, a) * 9 + 360 + ccw(a, b) * 9 + cw(b, c) * 9
        res.append(str(deg))
    return "\n".join(res) + "\n"
