"""UVa 941 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import islice, permutations
from math import factorial

def solve(s: str) -> str:
    tok = s.split()
    res = []
    for i in range(int(tok[0])):
        word, n = sorted(tok[1 + 2 * i]), int(tok[2 + 2 * i])
        if len(word) <= 7:
            res.append("".join(next(islice(permutations(word), n, None))))
            continue
        out = []
        while word:
            f = factorial(len(word) - 1)
            out.append(word.pop(n // f))
            n %= f
        res.append("".join(out))
    return "\n".join(res) + "\n"
