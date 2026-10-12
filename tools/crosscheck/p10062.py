"""UVa 10062 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter

def solve(s: str) -> str:
    blocks = []
    for line in s.split("\n")[:-1]:
        c = Counter(ord(ch) for ch in line)
        blocks.append("".join(f"{a} {n}\n" for a, n in sorted(c.items(), key=lambda kv: (kv[1], -kv[0]))))
    return "\n".join(blocks)
