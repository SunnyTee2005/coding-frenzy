"""UVa 11220 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    t = int(lines[0])
    p, blocks = 2, []
    for c in range(1, t + 1):
        out = [f"Case #{c}:"]
        while p < len(lines) and lines[p].strip():
            dec = ""
            for w in lines[p].split():
                if len(w) > len(dec):
                    dec += w[len(dec)]
            out.append(dec)
            p += 1
        p += 1
        blocks.append("".join(o + "\n" for o in out))
    return "\n".join(blocks)
