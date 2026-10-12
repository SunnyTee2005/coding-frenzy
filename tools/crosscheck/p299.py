"""UVa 299 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    res = []
    for i in range(int(lines[0])):
        p = list(map(int, lines[2 + 2 * i].split()))
        swaps = 0
        for a in range(len(p)):  # 泡沫排序實際做一次
            for b in range(len(p) - 1 - a):
                if p[b] > p[b + 1]:
                    p[b], p[b + 1] = p[b + 1], p[b]
                    swaps += 1
        res.append(f"Optimal train swapping takes {swaps} swaps.")
    return "\n".join(res) + "\n"
