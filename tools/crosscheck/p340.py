"""UVa 340 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    v = list(map(int, s.split()))
    p, game, res = 0, 0, []
    while v[p] != 0:
        n = v[p]; p += 1
        code = v[p:p + n]; p += n
        game += 1
        res.append(f"Game {game}:")
        while True:
            g = v[p:p + n]; p += n
            if not any(g):
                break
            strong = sum(a == b for a, b in zip(code, g))
            # 弱配對：拿掉強配對後，逐一配對剩下相同的數字
            rest_code = [a for a, b in zip(code, g) if a != b]
            rest_g = [b for a, b in zip(code, g) if a != b]
            weak = 0
            for x in rest_g:
                if x in rest_code:
                    rest_code.remove(x)
                    weak += 1
            res.append(f"    ({strong},{weak})")
    return "\n".join(res) + "\n"
