"""UVa 11349 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    t, p, res = int(lines[0]), 1, []
    for c in range(1, t + 1):
        n = int(lines[p].split("=")[1]); p += 1
        flat = [int(x) for line in lines[p:p + n] for x in line.split()]
        p += n
        ok = min(flat) >= 0 and flat == flat[::-1]
        res.append(f"Test #{c}: {'Symmetric.' if ok else 'Non-symmetric.'}")
    return "\n".join(res) + "\n"
