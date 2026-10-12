"""UVa 10327 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = list(map(int, s.split()))
    i, res = 0, []
    while i < len(t):
        n = t[i]; a = t[i + 1:i + 1 + n]; i += 1 + n
        # 用合併排序計算逆序數
        def count(v):
            if len(v) <= 1:
                return v, 0
            l, x = count(v[:len(v) // 2]); r, y = count(v[len(v) // 2:])
            merged, inv, p, q = [], x + y, 0, 0
            while p < len(l) and q < len(r):
                if l[p] <= r[q]:
                    merged.append(l[p]); p += 1
                else:
                    merged.append(r[q]); q += 1; inv += len(l) - p
            return merged + l[p:] + r[q:], inv
        res.append(f"Minimum exchange operations : {count(a)[1]}")
    return "\n".join(res) + "\n"
