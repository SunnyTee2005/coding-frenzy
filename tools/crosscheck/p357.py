"""UVa 357 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    xs = list(map(int, s.split()))
    res = []
    memo = {}
    def count(n, i):
        # 用 coins[i:] 湊出 n 的方法數；最後一種硬幣（1 分）只有一種方法
        coins = (50, 25, 10, 5, 1)
        if i == 4:
            return 1
        key = (n, i)
        if key not in memo:
            memo[key] = sum(count(n - j * coins[i], i + 1) for j in range(n // coins[i] + 1))
        return memo[key]
    for n in xs:
        m = count(n, 0)
        res.append(f"There is only 1 way to produce {n} cents change." if m == 1 else f"There are {m} ways to produce {n} cents change.")
    return "\n".join(res) + "\n"
