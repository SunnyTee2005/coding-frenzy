"""UVa 1587 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from collections import Counter
from itertools import combinations_with_replacement

def solve(s: str) -> str:
    v = list(map(int, s.split()))
    res = []
    for i in range(0, len(v), 12):
        faces = Counter(tuple(sorted(v[i + 2 * j:i + 2 * j + 2])) for j in range(6))
        dims = sorted({x for f in faces for x in f})
        ok = any(Counter([(a, b), (a, b), (a, c), (a, c), (b, c), (b, c)]) == faces
                 for a, b, c in combinations_with_replacement(dims, 3))
        res.append("POSSIBLE" if ok else "IMPOSSIBLE")
    return "\n".join(res) + "\n"
