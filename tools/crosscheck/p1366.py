"""UVa 1366 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from functools import lru_cache

def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    res = []
    while True:
        n, m = next(it), next(it)
        if n == 0 and m == 0:
            break
        Y = [[next(it) for _ in range(m)] for _ in range(n)]
        B = [[next(it) for _ in range(m)] for _ in range(n)]
        import sys
        sys.setrecursionlimit(10000)

        @lru_cache(maxsize=None)
        def best(r, c):
            # 左上角 r 列 c 行的最佳值：最下面一列全部往西送，或最右邊一行全部往北送
            if r == 0 or c == 0:
                return 0
            return max(best(r - 1, c) + sum(Y[r - 1][:c]), best(r, c - 1) + sum(B[i][c - 1] for i in range(r)))
        res.append(str(best(n, m)))
    return "\n".join(res) + "\n"
