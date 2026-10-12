"""UVa 580 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n == 0:
            break
        if n <= 16:
            res.append(str(sum(1 for m in range(1 << n) if "111" in format(m, f"0{n}b"))))
            continue
        # 狀態：結尾連續 U 的個數（0~2），以及是否已經出現 UUU
        dp = {(0, False): 1}
        for _ in range(n):
            new = {}
            for (run, hit), c in dp.items():
                for nxt in ((0, hit), (run + 1, hit or run + 1 >= 3)):
                    key = (min(nxt[0], 3), nxt[1])
                    new[key] = new.get(key, 0) + c
            dp = new
        res.append(str(sum(c for (run, hit), c in dp.items() if hit)))
    return "\n".join(res) + "\n"
