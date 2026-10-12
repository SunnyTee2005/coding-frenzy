"""UVa 1587 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1587-{kind}-{k}")
out = sys.stdout.write

cases = []
for _ in range(rng.randint(3, 120)):
    hi = rng.choice([3, 20, 10000])
    a, b, c = (rng.randint(1, hi) for _ in range(3))
    faces = [(a, b), (a, b), (a, c), (a, c), (b, c), (b, c)]
    if rng.random() < 0.5:
        i = rng.randrange(6)
        faces[i] = (faces[i][0], rng.randint(1, hi)) if rng.random() < 0.5 else (rng.randint(1, hi), rng.randint(1, hi))
    faces = [f if rng.random() < 0.5 else f[::-1] for f in faces]
    rng.shuffle(faces)
    cases.append(faces)
if kind == "hidden" and k == 1:
    cases = [[(1, 1)] * 6, [(1, 2)] * 6, [(1, 2), (1, 2), (1, 2), (1, 2), (2, 2), (2, 2)], [(1, 2), (2, 1), (1, 1), (1, 1), (2, 2), (2, 2)],
             [(1, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 2)]]
out("".join("".join(f"{w} {h}\n" for w, h in c) for c in cases))
