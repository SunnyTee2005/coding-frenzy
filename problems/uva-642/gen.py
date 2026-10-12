"""UVa 642 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"642-{kind}-{k}")
out = sys.stdout.write

alpha = "aeinrst"
dictionary = sorted({"".join(rng.choice(alpha) for _ in range(rng.randint(1, 6))) for _ in range(rng.randint(1, 100))})
queries = []
for _ in range(rng.randint(1, 40)):
    if rng.random() < 0.7:
        w = list(rng.choice(dictionary)); rng.shuffle(w); queries.append("".join(w))
    else:
        queries.append("".join(rng.choice(alpha + "xyz") for _ in range(rng.randint(1, 6))))
rng.shuffle(dictionary)
out("".join(w + "\n" for w in dictionary) + "XXXXXX\n" + "".join(q + "\n" for q in queries) + "XXXXXX\n")
