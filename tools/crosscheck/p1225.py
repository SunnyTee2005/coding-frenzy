"""UVa 1225 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split(); res = []
    for n in map(int, t[1:1 + int(t[0])]):
        d = ''.join(map(str, range(1, n + 1)))
        res.append(' '.join(str(d.count(str(i))) for i in range(10)))
    return '\n'.join(res) + '\n'
