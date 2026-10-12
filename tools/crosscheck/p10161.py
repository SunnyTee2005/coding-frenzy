"""UVa 10161 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from math import isqrt

def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        k = isqrt(n - 1) + 1          # 第 k 層：(k-1)^2 < n <= k^2
        pos = n - (k - 1) ** 2        # 層內第幾格（1 起算），共 2k-1 格
        if k % 2 == 1:
            # 奇數層：從 (k,1) 往上到 (k,k)，再往左到 (1,k)
            x, y = (k, pos) if pos <= k else (2 * k - pos, k)
        else:
            # 偶數層：從 (1,k) 往右到 (k,k)，再往下到 (k,1)
            x, y = (pos, k) if pos <= k else (k, 2 * k - pos)
        res.append(f"{x} {y}")
    return "\n".join(res) + "\n"
