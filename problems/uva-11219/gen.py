"""UVa 11219 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11219-{kind}-{k}")
out = sys.stdout.write

import datetime
def rdate(y0, y1):
    d = datetime.date(y0, 1, 1) + datetime.timedelta(days=rng.randint(0, (datetime.date(y1, 12, 31) - datetime.date(y0, 1, 1)).days))
    return d
def fmt(d):
    return f"{d.day:02d}/{d.month:02d}/{d.year:04d}"
cases = []
for _ in range(rng.randint(5, 200 if kind == "hidden" else 20)):
    cur = rdate(1900, 2100)
    r = rng.random()
    if r < 0.15:
        b = cur + datetime.timedelta(days=rng.randint(1, 400))
    elif r < 0.25:
        b = cur.replace(year=max(1, cur.year - rng.randint(130, 140))) if not (cur.month == 2 and cur.day == 29) else cur
    elif r < 0.35:
        b = cur
    else:
        b = rdate(max(1, cur.year - 130), cur.year)
        if b > cur:
            b = cur
    cases.append((cur, b))
if kind == "hidden" and k == 1:
    D = datetime.date
    cases = [(D(2005, 2, 28), D(2004, 2, 29)), (D(2008, 2, 29), D(2004, 2, 29)), (D(2007, 1, 1), D(2007, 1, 2)),
             (D(2007, 1, 2), D(2007, 1, 2)), (D(2007, 6, 9), D(1877, 6, 9)), (D(2007, 6, 9), D(1877, 6, 10)),
             (D(2007, 6, 8), D(1876, 6, 9))]
out(f"{len(cases)}\n" + "".join(f"\n{fmt(c)}\n{fmt(b)}\n" for c, b in cases))
