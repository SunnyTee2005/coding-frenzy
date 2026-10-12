"""UVa 10190 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for n, m in zip(v[0::2], v[1::2]):
        seq = [n]
        ok = n >= 2 and m >= 2
        while ok and seq[-1] != 1:
            if seq[-1] % m:
                ok = False
            else:
                seq.append(seq[-1] // m)
        res.append(" ".join(map(str, seq)) if ok else "Boring!")
    return "\n".join(res) + "\n"
