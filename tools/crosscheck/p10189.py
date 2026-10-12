"""UVa 10189 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    lines = s.splitlines(); i = 0; fields = []
    while True:
        n, m = map(int, lines[i].split()); i += 1
        if n == 0 and m == 0: break
        g = lines[i:i + n]; i += n
        rows = []
        for r in range(n):
            row = ''
            for c in range(m):
                if g[r][c] == '*': row += '*'; continue
                row += str(sum(g[a][b] == '*' for a in range(r-1, r+2) for b in range(c-1, c+2) if 0 <= a < n and 0 <= b < m))
            rows.append(row)
        fields.append(f'Field #{len(fields)+1}:\n' + '\n'.join(rows) + '\n')
    return '\n'.join(fields)
