"""UVa 725 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import permutations

def solve(s: str) -> str:
    sols = {}
    for p in permutations("0123456789", 5):
        den = "".join(p)
        rest = set("0123456789") - set(p)
        for n in range(2, 80):
            num = int(den) * n
            if num < 100000 and set(f"{num:05d}") == rest:
                sols.setdefault(n, []).append((num, den))
    blocks = []
    for n in map(int, s.split()):
        if n == 0:
            break
        found = sorted(sols.get(n, []))
        if found:
            blocks.append("".join(f"{num:05d} / {den} = {n}\n" for num, den in found))
        else:
            blocks.append(f"There are no solutions for {n}.\n")
    return "\n".join(blocks)
