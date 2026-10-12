"""UVa 10539 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


import bisect

_cache = []

def table():
    if not _cache:
        n = 10 ** 6
        sieve = bytearray([1]) * (n + 1)
        sieve[0] = sieve[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        vals = []
        for p in range(2, n + 1):
            if sieve[p]:
                x = p * p
                while x < 10 ** 12:
                    vals.append(x)
                    x *= p
        _cache.append(sorted(vals))
    return _cache[0]

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    t = table()
    return "".join(f"{bisect.bisect_right(t, b) - bisect.bisect_left(t, a)}\n" for a, b in zip(v[1::2], v[2::2]))
