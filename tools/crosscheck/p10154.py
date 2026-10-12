"""UVa 10154 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import permutations

def best_brute(ts):
    best = 0
    n = len(ts)
    for mask in range(1, 1 << n):
        chosen = [ts[i] for i in range(n) if mask >> i & 1]
        if len(chosen) <= best:
            continue
        for order in permutations(chosen):  # order[0] 在最上面
            load, ok = 0, True
            for w, s in order:
                load += w
                if load > s:
                    ok = False
                    break
            if ok:
                best = len(chosen)
                break
    return best

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    ts = list(zip(v[0::2], v[1::2]))
    if len(ts) <= 7:
        return f"{best_brute(ts)}\n"
    # 大資料：依「力量」由小到大，dp[c] = 疊 c 隻的最小總重
    ts.sort(key=lambda t: t[1])
    dp = {0: 0}
    for w, st in ts:
        new = dict(dp)
        for c, tot in dp.items():
            if tot + w <= st and tot + w < new.get(c + 1, float("inf")):
                new[c + 1] = tot + w
        dp = new
    return f"{max(dp)}\n"
