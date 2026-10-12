"""UVa 13171 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


MIX = {"M": "M", "Y": "Y", "C": "C", "R": "MY", "B": "MYC", "G": "YC", "V": "MC", "W": ""}

def solve(s: str) -> str:
    tok = s.split()
    res = []
    for i in range(int(tok[0])):
        m, y, c, img = tok[1 + 4 * i:5 + 4 * i]
        left = {"M": int(m), "Y": int(y), "C": int(c)}
        for p in img:
            for prim in MIX[p]:
                left[prim] -= 1
        res.append("NO" if min(left.values()) < 0 else f"YES {left['M']} {left['Y']} {left['C']}")
    return "\n".join(res) + "\n"
