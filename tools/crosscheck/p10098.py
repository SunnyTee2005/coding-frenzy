"""UVa 10098 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import permutations

def solve(s: str) -> str:
    t = s.split()
    out = ""
    for w in t[1:1 + int(t[0])]:
        out += "".join(p + "\n" for p in sorted(set("".join(x) for x in permutations(w)))) + "\n"
    return out
