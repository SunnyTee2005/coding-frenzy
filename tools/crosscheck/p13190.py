"""UVa 13190 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    i, out = 1, []
    for _ in range(int(t[0])):
        n, k = int(t[i]), int(t[i + 1]); i += 2
        meds = [(t[i + 2 * j], int(t[i + 2 * j + 1])) for j in range(n)]; i += 2 * n
        doses = sorted((f * m, j) for j, (_, f) in enumerate(meds) for m in range(1, k + 1))[:k]
        out.extend(f"{tm} {meds[j][0]}" for tm, j in doses)
    return "\n".join(out) + "\n"
