"""UVa 10633 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for x in map(int, s.split()):
        if x == 0:
            break
        found = []
        # 反過來驗算：N 的最後一位 d，N - N//10 必須等於 x
        base = x * 10 // 9
        for n in range(base - 20, base + 21):
            if n >= 10 and n - n // 10 == x:
                found.append(n)
        res.append(" ".join(map(str, sorted(found))))
    return "\n".join(res) + "\n"
