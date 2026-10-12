"""UVa 10242 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def mm(t):
    neg = t.startswith("-")
    whole, frac = t.lstrip("-").split(".")
    v = int(whole) * 1000 + int(frac.ljust(3, "0")[:3])
    return -v if neg else v

def fmt(v):
    return f"{'-' if v < 0 else ''}{abs(v) // 1000}.{abs(v) % 1000:03d}"

def solve(s: str) -> str:
    res = []
    for line in s.split("\n"):
        if not line.strip():
            continue
        v = list(map(mm, line.split()))
        p = [(v[0], v[1]), (v[2], v[3]), (v[4], v[5]), (v[6], v[7])]
        shared = next(q for q in p[:2] if q in p[2:])
        others = [q for q in p if q != shared]
        res.append(f"{fmt(others[0][0] + others[1][0] - shared[0])} {fmt(others[0][1] + others[1][1] - shared[1])}")
    return "\n".join(res) + "\n"
