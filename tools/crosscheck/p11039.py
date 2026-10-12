"""UVa 11039 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    i, res = 1, []
    for _ in range(t[0]):
        n = t[i]; v = sorted(t[i + 1:i + 1 + n], key=abs); i += 1 + n
        # 動態規劃：以藍 / 紅結尾的最高樓層數
        end_blue = end_red = 0
        for x in v:
            if x > 0:
                end_blue = max(end_blue, end_red + 1)
            else:
                end_red = max(end_red, end_blue + 1)
        res.append(str(max(end_blue, end_red)))
    return "\n".join(res) + "\n"
