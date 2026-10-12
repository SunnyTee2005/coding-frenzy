"""UVa 673 測資：python3 gen.py <public|hidden> <編號>"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"673-{kind}-{k}")


def balanced(n):
    if n <= 0:
        return ""
    inner = rng.randint(0, n - 1)
    o, c = rng.choice(["()", "[]"])
    return o + balanced(inner) + c + balanced(n - 1 - inner)


def mutate(s):
    if not s:
        return rng.choice("()[]")
    s = list(s)
    i = rng.randrange(len(s))
    s[i] = rng.choice("()[]")
    return "".join(s)


def case():
    s = balanced(rng.randint(0, 64))
    return s if rng.random() < 0.5 else mutate(s)


if kind == "hidden" and k == 1:
    lines = ["", "(", ")", "[]", "][", "([)]", "(((", "()()()", "[" * 64 + "]" * 64, "(" * 64 + "]" * 64]
elif kind == "hidden" and k >= 8:
    lines = [case() for _ in range(3000)]
else:
    lines = [case() for _ in range(rng.randint(3, 60))]
sys.stdout.write(f"{len(lines)}\n" + "".join(l + "\n" for l in lines))
