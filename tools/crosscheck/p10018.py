"""UVa 10018 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split(); res = []
    for p in map(int, t[1:1 + int(t[0])]):
        k = 0
        while True:
            p += int(str(p)[::-1]); k += 1
            if str(p) == str(p)[::-1]: break
        res.append(f'{k} {p}')
    return '\n'.join(res) + '\n'
