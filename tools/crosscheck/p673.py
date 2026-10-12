"""UVa 673 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.split('\n'); n = int(lines[0]); res = []
    for line in lines[1:1 + n]:
        prev = None
        while prev != line:
            prev = line; line = line.replace('()', '').replace('[]', '')
        res.append('Yes' if line == '' else 'No')
    return '\n'.join(res) + '\n'
