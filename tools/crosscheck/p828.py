"""UVa 828 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decode(msg, L, n):
    inL = set(L)
    memo = {}
    def go(i, m):
        # 回傳從位置 i、計數 m 開始的所有解（最多 2 個）
        key = (i, m % len(L))
        if key in memo:
            return memo[key]
        if i == len(msg):
            return [""]
        ch, sols = msg[i], []
        if ch == " ":
            sols = [" " + x for x in go(i + 1, m)]
        else:
            p = A[(A.index(ch) - n) % 26]
            if p not in inL:
                sols += [p + x for x in go(i + 1, m)]
            if ch == L[m % len(L)] and i + 2 < len(msg) and msg[i + 1] != " " and msg[i + 2] == L[(m + 1) % len(L)]:
                p = A[(A.index(msg[i + 1]) - n) % 26]
                if p in inL:
                    sols += [p + x for x in go(i + 3, m + 1)]
        memo[key] = sols[:2]
        return memo[key]
    sols = go(0, 0)
    return sols[0] if len(sols) == 1 else "error in encryption"

def solve(s: str) -> str:
    lines = s.split("\n")
    t, p, blocks = int(lines[0]), 1, []
    for _ in range(t):
        while not lines[p].strip():
            p += 1
        L, n, q = lines[p], int(lines[p + 1]), int(lines[p + 2])
        p += 3
        blocks.append("".join(decode(lines[p + i], L, n) + "\n" for i in range(q)))
        p += q
    return "\n".join(blocks)
