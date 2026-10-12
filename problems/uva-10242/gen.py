"""UVa 10242 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10242-{kind}-{k}")
out = sys.stdout.write

def pt():
    return (rng.randint(-5000000, 5000000), rng.randint(-5000000, 5000000))
def fmt(v):
    return f"{'-' if v < 0 else ''}{abs(v) // 1000}.{abs(v) % 1000:03d}"
lines = []
while len(lines) < rng.randint(3, 200):
    if rng.random() < 0.5:
        a, b, c = pt(), pt(), pt()
    else:
        a, b, c = [(rng.randint(-5, 5) * 500, rng.randint(-5, 5) * 500) for _ in range(3)]
    if len({a, b, c}) < 3:
        continue
    s1 = [a, b] if rng.random() < 0.5 else [b, a]   # 共用點 a
    s2 = [a, c] if rng.random() < 0.5 else [c, a]
    lines.append(" ".join(f"{fmt(p[0])} {fmt(p[1])}" for p in s1 + s2))
out("".join(l + "\n" for l in lines))
