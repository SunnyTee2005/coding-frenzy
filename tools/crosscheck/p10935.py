"""UVa 10935 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    res = []
    for n in map(int, s.split()):
        if n == 0: break
        q = list(range(1, n + 1)); disc = []
        while len(q) > 1:
            disc.append(q.pop(0)); q.append(q.pop(0))
        res.append(('Discarded cards: ' + ', '.join(map(str, disc))).rstrip())
        res.append(f'Remaining card: {q[0]}')
    return '\n'.join(res) + '\n'
