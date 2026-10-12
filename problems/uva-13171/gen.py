"""UVa 13171 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"13171-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(1, 20)):
    n = rng.randint(1, 100000 if (kind == "hidden" and k == 10 and not cases) else 300)
    s = "".join(rng.choice("MYCRBGVW") for _ in range(n))
    need = [sum(s.count(ch) for ch in "MRBV"), sum(s.count(ch) for ch in "YRBG"), sum(s.count(ch) for ch in "CBGV")]
    have = [max(0, x + rng.choice([0, 0, 1, 5, -1, rng.randint(-3, 100)])) for x in need]
    cases.append((have, s))
if kind == "hidden" and k == 1:
    cases = [([0, 0, 0], "W"), ([0, 0, 0], "WWWW"), ([1, 0, 0], "M"), ([0, 0, 0], "M"), ([1, 1, 1], "B"), ([1, 1, 0], "B")]
out(f"{len(cases)}\n" + "".join(f"{h[0]} {h[1]} {h[2]} {s}\n" for h, s in cases))
