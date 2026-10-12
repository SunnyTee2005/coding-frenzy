"""UVa 642 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    i = t.index("XXXXXX")
    words = sorted(t[:i])
    queries = t[i + 1:t.index("XXXXXX", i + 1)]
    out = []
    for q in queries:
        hits = [w for w in words if sorted(w) == sorted(q)]
        out.extend(hits or ["NOT A VALID WORD"])
        out.append("******")
    return "\n".join(out) + "\n"
