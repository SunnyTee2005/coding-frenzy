"""UVa 11576 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    i = 1
    res = []
    for _ in range(int(t[0])):
        k, w = int(t[i]), int(t[i + 1]); i += 2
        words = t[i:i + w]; i += w
        total = k
        for a, b in zip(words, words[1:]):
            overlap = max(m for m in range(k + 1) if a.endswith(b[:m]) and (m == 0 or a[-m:] == b[:m]))
            total += k - overlap
        res.append(str(total))
    return "\n".join(res) + "\n"
