"""UVa 10101 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


UNITS = [(10000000, "kuti"), (100000, "lakh"), (1000, "hajar"), (100, "shata")]

def words(n):
    parts = []
    for size, name in UNITS:
        if n >= size:
            parts += words(n // size) + [name]
            n %= size
    if n:
        parts.append(str(n))
    return parts

def solve(s: str) -> str:
    return "".join(f"{i + 1:4d}. " + " ".join(words(n)) + "\n" for i, n in enumerate(map(int, s.split())))
