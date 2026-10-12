"""UVa 1203 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    regs = []
    i = 0
    while lines[i] != "#":
        _, q, p = lines[i].split()
        regs.append((int(q), int(p)))
        i += 1
    k = int(lines[i + 1])
    # 每個查詢的前 k 次回報時間都列出來，排序後取前 k 個
    events = sorted((p * t, q) for q, p in regs for t in range(1, k + 1))
    return "".join(f"{q}\n" for _, q in events[:k])
