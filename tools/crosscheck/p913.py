"""UVa 913 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        rows = (n + 1) // 2           # 第幾列
        before = (rows - 1) ** 2      # 前面各列共有幾個奇數
        nums = [2 * (before + i) + 1 for i in range(n - 3, n)]
        res.append(str(sum(nums)))
    return "\n".join(res) + "\n"
