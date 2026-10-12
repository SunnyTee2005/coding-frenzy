"""UVa 729 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import combinations

def solve(s: str) -> str:
    t = list(map(int, s.split()))
    blocks = []
    for i in range(t[0]):
        n, h = t[1 + 2 * i], t[2 + 2 * i]
        strings = sorted("".join("1" if j in ones else "0" for j in range(n)) for ones in combinations(range(n), h))
        blocks.append("".join(x + "\n" for x in strings))
    return "\n".join(blocks)
