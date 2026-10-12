"""UVa 10273 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from math import lcm

def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        n = next(it)
        cows = []
        for _ in range(n):
            t = next(it)
            cows.append([next(it) for _ in range(t)])
        alive = set(range(n))
        day = last = 0
        while alive:
            # 剩下的牛的週期最小公倍數內都沒有牛被吃，就永遠不會再有
            period = lcm(*(len(cows[i]) for i in alive))
            eaten = False
            for _ in range(period):
                day += 1
                today = {i: cows[i][(day - 1) % len(cows[i])] for i in alive}
                low = min(today.values())
                who = [i for i, v in today.items() if v == low]
                if len(who) == 1:
                    alive.remove(who[0]); last = day; eaten = True
                    break
            if not eaten:
                break
        res.append(f"{len(alive)} {last}")
    return "\n".join(res) + "\n"
