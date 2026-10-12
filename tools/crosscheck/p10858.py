"""UVa 10858 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def facts(n, smallest):
    # 回傳把 n 拆成 >= smallest、非遞減因數的所有方法（包含只有 n 本身）
    res = [[n]] if n >= smallest else []
    f = smallest
    while f * f <= n:
        if n % f == 0:
            res += [[f] + rest for rest in facts(n // f, f)]
        f += 1
    return res

def solve(s: str) -> str:
    out = []
    for n in map(int, s.split()):
        if n == 0:
            break
        ways = sorted(w for w in facts(n, 2) if len(w) >= 2)
        out.append(str(len(ways)))
        out += [" ".join(map(str, w)) for w in ways]
    return "\n".join(out) + "\n"
