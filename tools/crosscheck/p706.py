"""UVa 706 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    # 用 3x5 的範本放大：每個數字的七段開關
    on = {
        "0": "1110111", "1": "0010010", "2": "1011101", "3": "1011011", "4": "0111010",
        "5": "1101011", "6": "1101111", "7": "1010010", "8": "1111111", "9": "1111011",
    }  # 順序：上、左上、右上、中、左下、右下、下
    t = s.split()
    out = []
    for i in range(0, len(t), 2):
        size, num = int(t[i]), t[i + 1]
        if size == 0 and num == "0":
            break
        rows = [[] for _ in range(2 * size + 3)]
        for d in num:
            top, ul, ur, mid, ll, lr, bot = (c == "1" for c in on[d])
            h = lambda flag: " " + ("-" if flag else " ") * size + " "
            v = lambda l, r: ("|" if l else " ") + " " * size + ("|" if r else " ")
            cells = [h(top)] + [v(ul, ur)] * size + [h(mid)] + [v(ll, lr)] * size + [h(bot)]
            for r, cell in enumerate(cells):
                rows[r].append(cell)
        out.extend(" ".join(r) for r in rows)
        out.append("")
    return "\n".join(out) + "\n"
