"""UVa 543 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    xs = []
    for x in map(int, s.split()):
        if x == 0:
            break
        xs.append(x)
    n = max(xs)
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    res = []
    for x in xs:
        a = next((a for a in range(3, x // 2 + 1, 2) if sieve[a] and sieve[x - a]), None)
        res.append(f"{x} = {a} + {x - a}" if a else "Goldbach's conjecture is wrong.")
    return "\n".join(res) + "\n"
