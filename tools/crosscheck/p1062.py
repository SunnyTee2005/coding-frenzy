"""UVa 1062 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for w in s.split():
        if w == "end":
            break
        # 最少堆數 = 最長嚴格遞增子序列長度（O(n^2) DP）
        best = [1] * len(w)
        for i in range(len(w)):
            for j in range(i):
                if w[j] < w[i] and best[j] + 1 > best[i]:
                    best[i] = best[j] + 1
        res.append(f"Case {len(res) + 1}: {max(best)}")
    return "\n".join(res) + "\n"
