"""UVa 948 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split(); fib = [1, 2]
    while fib[-1] < 10**8: fib.append(fib[-1] + fib[-2])
    res = []
    for x in map(int, t[1:1 + int(t[0])]):
        left, bits = x, ''
        for f in reversed(fib):
            if f <= left: left -= f; bits += '1'
            elif bits: bits += '0'
        res.append(f'{x} = {bits} (fib)')
    return '\n'.join(res) + '\n'
