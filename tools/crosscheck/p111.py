"""UVa 111 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import bisect

def order(ranks):
    o = [0] * len(ranks)
    for event, r in enumerate(ranks):
        o[r - 1] = event
    return o

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    n = v[0]
    pos = {e: i for i, e in enumerate(order(v[1:1 + n]))}
    res = []
    for p in range(1 + n, len(v), n):
        # 兩個都是排列：LCS = 把學生順序換成正確位置後的最長遞增子序列
        seq = [pos[e] for e in order(v[p:p + n])]
        tails = []
        for x in seq:
            i = bisect.bisect_left(tails, x)
            tails[i:i + 1] = [x]
        res.append(str(len(tails)))
    return "\n".join(res) + "\n"
