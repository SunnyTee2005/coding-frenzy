"""UVa 11364 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    for _ in range(next(it)):
        xs = [next(it) for _ in range(next(it))]
        # 每個停車位置都試一次：從車子出發走遍所有店再回到車子
        res.append(str(min(2 * (max(xs + [p]) - min(xs + [p])) for p in range(100))))
    return "\n".join(res) + "\n"
