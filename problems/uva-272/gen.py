"""UVa 272 測資：python3 gen.py <public|hidden> <編號>"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"272-{kind}-{k}")
WORDS = "the quick brown fox jumps over lazy dog to be or not that is question a I said hello world".split()


def line(n_words):
    return " ".join(rng.choice(WORDS) for _ in range(n_words))


def text(n_lines, quote_rate):
    out = []
    quotes = 0
    for _ in range(n_lines):
        parts = []
        for w in line(rng.randint(0, 12)).split(" "):
            if rng.random() < quote_rate:
                parts.append('"' + w)
                quotes += 1
            else:
                parts.append(w)
        out.append(" ".join(parts))
    s = "\n".join(out) + "\n"
    if quotes % 2:
        s = s.rstrip("\n") + '"\n'
    return s


if kind == "hidden" and k == 1:
    # 邊界：沒有引號、空行、相鄰引號、行首行尾引號、跨行配對
    sys.stdout.write('no quotes here\n\n""\n"start and end"\n"multi\nline"\n   spaces   "x"   \n')
elif kind == "hidden" and k == 2:
    sys.stdout.write('"a" "b" "c" "d" "e" "f"\n' * 50)
elif kind == "hidden" and k >= 8:
    sys.stdout.write(text(250, 0.2))
else:
    sys.stdout.write(text(rng.randint(5, 60), 0.15))
