"""UVa 11240 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split("\n")
    res = []
    for line in lines[1:1 + int(lines[0])]:
        a = list(map(int, line.split()))[1:]
        # 貪心：保留目前子序列最後一個值，並讓它對下一步最有利
        length, last, down = 1, a[0], True
        for x in a[1:]:
            if down:
                if x < last:
                    length += 1; down = False
                last = x if x < last else max(last, x)
            else:
                if x > last:
                    length += 1; down = True
                last = x if x > last else min(last, x)
        res.append(str(length))
    return "\n".join(res) + "\n"
