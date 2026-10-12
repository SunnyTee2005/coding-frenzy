"""UVa 11743 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11743-{kind}-{k}")
out = sys.stdout.write

def luhn_fix(digits):
    # 讓最後一位使總和為 10 的倍數
    for last in range(10):
        d = digits[:15] + [last]
        s = sum((x * 2) // 10 + (x * 2) % 10 if i % 2 == 0 else x for i, x in enumerate(d))
        if s % 10 == 0:
            return d
def card():
    d = [rng.randint(0, 9) for _ in range(16)]
    if rng.random() < 0.5:
        d = luhn_fix(d)
    s = "".join(map(str, d))
    return " ".join(s[i:i + 4] for i in range(0, 16, 4))
cards = [card() for _ in range(rng.randint(3, 50))]
if kind == "hidden" and k == 1:
    cards = ["0000 0000 0000 0000", "9999 9999 9999 9995", "4111 1111 1111 1111", "1234 5678 9012 3456"]
out(f"{len(cards)}\n" + "".join(c + "\n" for c in cards))
