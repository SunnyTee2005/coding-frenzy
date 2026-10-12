"""UVa 11417 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    # 用尤拉函數：sum_{j<=N} sum_{d|j, d<j} d*phi(j/d)
    phi = list(range(501))
    for i in range(2, 501):
        if phi[i] == i:
            for j in range(i, 501, i):
                phi[j] -= phi[j] // i
    f = [0] * 501
    for d in range(1, 501):
        for m in range(2 * d, 501, d):
            f[m] += d * phi[m // d]
    pre = [0] * 501
    for n in range(1, 501):
        pre[n] = pre[n - 1] + f[n]
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        res.append(str(pre[n]))
    return "\n".join(res) + "\n"
