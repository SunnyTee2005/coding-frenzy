"""UVa 263 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        res.append(f"Original number was {n}")
        chain = [n]
        while True:
            d = sorted(str(n))
            hi, lo = int("".join(reversed(d))), int("".join(d))
            n = hi - lo
            res.append(f"{hi} - {lo} = {n}")
            if n in chain:
                break
            chain.append(n)
        res.append(f"Chain length {len(chain)}")
        res.append("")
    return "".join(r + "\n" for r in res)
