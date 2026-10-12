"""UVa 10226 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter
from decimal import Decimal, ROUND_HALF_EVEN

def solve(s: str) -> str:
    blocks = s.split("\n\n")[1:]
    outs = []
    for b in blocks:
        names = [l for l in b.split("\n") if l]
        if not names:
            continue
        c = Counter(names)
        outs.append("".join(f"{n} {100 * c[n] / len(names):.4f}\n" for n in sorted(c)))
    return "\n".join(outs)
