"""UVa 865 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"865-{kind}-{k}")
out = sys.stdout.write

LOW = "abcdefghijklmnopqrstuvwxyz"
TEXT = "The quick brown fox jumps over the lazy dog, 123 times! It's CPE day: (test) #42."
cases = []
for _ in range(rng.randint(1, 5)):
    plain = rng.choice([LOW, LOW.upper(), "".join(rng.sample(LOW, rng.randint(1, 26)))])
    sub = "".join(rng.sample(LOW + LOW.upper(), len(plain)))
    lines = []
    for _ in range(rng.randint(1, 15)):
        words = TEXT.split()
        line = " ".join(rng.choice(words) if rng.random() < 0.7 else "".join(rng.choice(LOW + LOW.upper() + "0123456789.,!?") for _ in range(rng.randint(1, 8)))
                        for _ in range(rng.randint(1, 9)))
        lines.append(line[:64].rstrip())
    cases.append((plain, sub, lines))
out(f"{len(cases)}\n\n" + "\n".join(f"{p}\n{s}\n" + "".join(l + "\n" for l in ls) for p, s, ls in cases))
