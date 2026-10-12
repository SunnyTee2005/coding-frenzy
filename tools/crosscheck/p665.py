"""UVa 665 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    tok = s.split()
    p = 1
    out = []
    for _ in range(int(tok[0])):
        n, k = int(tok[p]), int(tok[p + 1]); p += 2
        ws = []
        for _ in range(k):
            c = int(tok[p]); p += 1
            left = list(map(int, tok[p:p + c])); right = list(map(int, tok[p + c:p + 2 * c])); p += 2 * c
            ws.append((left, right, tok[p])); p += 1
        # 逐一假設「第 c 枚是假幣、比較重/比較輕」，檢查是否和所有秤重結果一致
        possible = set()
        for coin in range(1, n + 1):
            for d in (1, -1):
                ok = True
                for left, right, res in ws:
                    w = (d if coin in left else 0) - (d if coin in right else 0)
                    if res != ("=" if w == 0 else (">" if w > 0 else "<")):
                        ok = False
                        break
                if ok:
                    possible.add(coin)
        out.append(str(possible.pop()) if len(possible) == 1 else "0")
    return "\n\n".join(out) + "\n"
