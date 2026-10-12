"""UVa 1118 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


# 小的 n 用遞迴式 S(n,m) = m*S(n-1,m) + S(n-1,m-1)（mod 2）直接算，驗證公式
SMALL = 60
S = [[0] * (SMALL + 1) for _ in range(SMALL + 1)]
S[0][0] = 1
for i in range(1, SMALL + 1):
    for j in range(1, i + 1):
        S[i][j] = (j * S[i - 1][j] + S[i - 1][j - 1]) % 2

def parity(n, m):
    # Lucas 定理：C(a, b) 為奇數 ⇔ b 的每個 1 位元 a 都有
    a, b = n - (m + 2) // 2, (m - 1) // 2
    return 1 if a >= 0 and (a | b) == a else 0

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(v[0]):
        n, m = v[1 + 2 * i], v[2 + 2 * i]
        p = parity(n, m)
        if n <= SMALL:
            assert p == S[n][m], (n, m)
        res.append(str(p))
    return "\n".join(res) + "\n"
