"""UVa 10035 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for line in s.splitlines():
        a, b = line.split()
        if a == '0' and b == '0': break
        a, b = a.zfill(12), b.zfill(12)
        c = n = 0
        for x, y in zip(reversed(a), reversed(b)):
            c = 1 if int(x) + int(y) + c >= 10 else 0
            n += c
        res.append('No carry operation.' if n == 0 else '1 carry operation.' if n == 1 else f'{n} carry operations.')
    return '\n'.join(res) + '\n'
