"""UVa 111 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"111-{kind}-{k}")
out = sys.stdout.write

n = rng.randint(2, 20)
def perm():
    p = list(range(1, n + 1)); rng.shuffle(p); return p
correct = perm()
students = [perm() for _ in range(rng.randint(1, 100))]
students += [correct[:]]
rng.shuffle(students)
out(f"{n}\n{' '.join(map(str, correct))}\n" + "".join(" ".join(map(str, s)) + "\n" for s in students))
