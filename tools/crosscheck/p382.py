"""UVa 382 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = ["PERFECTION OUTPUT"]
    for n in map(int, s.split()):
        if n == 0:
            break
        t = sum(d + (n // d if d * d != n and d != 1 else 0) for d in range(1, int(n ** 0.5) + 1) if n % d == 0)
        if n == 1:
            t = 0
        word = "PERFECT" if t == n else ("DEFICIENT" if t < n else "ABUNDANT")
        res.append(f"{n:>5}  {word}")
    res.append("END OF OUTPUT")
    return "\n".join(res) + "\n"
