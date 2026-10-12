"""UVa 13055 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    st, res = [], []
    for line in lines[1:1 + int(lines[0])]:
        parts = line.split()
        if parts[0] == "Sleep":
            st.append(parts[1])
        elif parts[0] == "Kick":
            if st:
                st.pop()
        else:
            res.append(st[-1] if st else "Not in a dream")
    return "".join(r + "\n" for r in res)
