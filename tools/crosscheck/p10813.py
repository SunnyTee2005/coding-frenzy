"""UVa 10813 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    p, res = 1, []
    for _ in range(v[0]):
        nums = v[p:p + 24]; p += 24
        cells = nums[:12] + [0] + nums[12:]
        pos = {x: i for i, x in enumerate(cells) if x}
        lines = [set(range(r * 5, r * 5 + 5)) for r in range(5)] + [set(range(c, 25, 5)) for c in range(5)]
        lines += [{0, 6, 12, 18, 24}, {4, 8, 12, 16, 20}]
        marked = {12}
        order = v[p:p + 75]; p += 75
        for k, x in enumerate(order, 1):
            if x in pos:
                marked.add(pos[x])
            if any(l <= marked for l in lines):
                res.append(f"BINGO after {k} numbers announced")
                break
    return "\n".join(res) + "\n"
