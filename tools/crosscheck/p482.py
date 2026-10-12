"""UVa 482 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = [l for l in s.split("\n")[1:] if l.strip()]
    blocks = []
    for p_line, v_line in zip(lines[0::2], lines[1::2]):
        p, v = list(map(int, p_line.split())), v_line.split()
        out = dict(zip(p, v))
        blocks.append("".join(out[i] + "\n" for i in range(1, len(p) + 1)))
    return "\n".join(blocks)
