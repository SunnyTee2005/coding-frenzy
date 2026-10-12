"""UVa 10908 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10908-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 5 if k < 10 else 3)):
    m, n = rng.randint(1, 40), rng.randint(1, 40)
    if kind == "hidden" and k == 10:
        m, n = rng.randint(80, 100), rng.randint(80, 100)
    al = rng.choice(["a", "ab", "abc", "abcdefghij"])
    g = [[al[0]] * n for _ in range(m)]
    for _ in range(rng.randint(0, 2 * (m + n))):
        if rng.random() < 0.3:
            x, y = rng.randrange(m), rng.randrange(n)
            h, w = rng.randint(1, m), rng.randint(1, n)
            ch = rng.choice(al)
            for i in range(x, min(m, x + h)):
                for j in range(y, min(n, y + w)):
                    g[i][j] = ch
        else:
            g[rng.randrange(m)][rng.randrange(n)] = rng.choice(al)
    qs = [(rng.randrange(m), rng.randrange(n)) for _ in range(rng.randint(1, 20))]
    cases.append((m, n, ["".join(r) for r in g], qs))
if kind == "hidden" and k == 1:
    cases = [(1, 1, ["z"], [(0, 0)]), (3, 3, ["aaa", "aaa", "aaa"], [(1, 1), (0, 0), (2, 1)]),
             (5, 5, ["aaaaa"] * 5, [(2, 2), (1, 2), (2, 3)])]
out(f"{len(cases)}\n" + "".join(f"{m} {n} {len(qs)}\n" + "".join(r + "\n" for r in g) + "".join(f"{r} {c}\n" for r, c in qs)
                             for m, n, g, qs in cases))
