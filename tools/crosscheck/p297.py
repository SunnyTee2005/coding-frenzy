"""UVa 297 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def pixels(t):
    # 回傳黑色像素的集合（座標以 1024 個格子編號），四個象限的順序不影響總數
    out = set()
    def go(i, x, y, size):
        ch = t[i]
        if ch == "p":
            h = size // 2
            i += 1
            for dx, dy in ((h, 0), (0, 0), (0, h), (h, h)):
                i = go(i, x + dx, y + dy, h)
            return i
        if ch == "f":
            out.update((a, b) for a in range(x, x + size) for b in range(y, y + size))
        return i + 1
    go(0, 0, 0, 32)
    return out

def solve(s: str) -> str:
    tok = s.split()
    return "".join(f"There are {len(pixels(tok[1 + 2 * i]) | pixels(tok[2 + 2 * i]))} black pixels.\n" for i in range(int(tok[0])))
