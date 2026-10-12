"""UVa 10258 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10258-{kind}-{k}")
out = sys.stdout.write

def case():
    people = rng.sample(range(1, 101), rng.randint(1, 12 if k < 8 else 60))
    subs, time = [], 0
    for _ in range(rng.randint(1, 60 if k < 8 else 300)):
        time += rng.randint(0, 5)
        subs.append(f"{rng.choice(people)} {rng.randint(1, 9)} {time} {rng.choice('CCIIIRUE')}")
    return "".join(s + "\n" for s in subs)
T = rng.randint(1, 4)
if kind == "hidden" and k == 1:
    out("2\n\n5 1 10 R\n7 1 3 E\n\n2 3 5 C\n2 3 6 I\n2 3 7 C\n1 1 5 I\n1 1 5 C\n")
else:
    out(f"{T}\n\n" + "\n".join(case() for _ in range(T)))
