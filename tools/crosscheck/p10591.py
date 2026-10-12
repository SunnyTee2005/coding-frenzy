"""UVa 10591 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i, n in enumerate(v[1:1 + v[0]]):
        x = n
        # 不快樂數一定會掉進含 4 的循環
        while x not in (1, 4):
            x = sum(int(d) ** 2 for d in str(x))
        res.append(f"Case #{i + 1}: {n} is {'a Happy' if x == 1 else 'an Unhappy'} number.")
    return "\n".join(res) + "\n"
