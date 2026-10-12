"""UVa 483 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"483-{kind}-{k}")
out = sys.stdout.write

WORDS = "I love you. You me We're a happy family! Hello, world: abc xyz 12345".split()
lines = []
for _ in range(rng.randint(3, 60)):
    parts = [rng.choice(WORDS) for _ in range(rng.randint(1, 12))]
    lines.append("".join(p + " " * rng.choice([1, 1, 1, 2]) for p in parts).rstrip())
out("".join(l + "\n" for l in lines))
