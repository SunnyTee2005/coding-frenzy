"""UVa 12195 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12195-{kind}-{k}")
out = sys.stdout.write

VAL = {"W": 64, "H": 32, "Q": 16, "E": 8, "S": 4, "T": 2, "X": 1}
def measure():
    if rng.random() < 0.5:  # 剛好 1 拍
        left, notes = 64, []
        while left:
            c = rng.choice([c for c, v in VAL.items() if v <= left])
            notes.append(c); left -= VAL[c]
        rng.shuffle(notes)
        m = "".join(notes)
        if rng.random() < 0.2:
            m += rng.choice("WHQESTX")
        return m
    return "".join(rng.choice("WHQESTX") for _ in range(rng.randint(1, 12)))
lines = ["/" + "/".join(measure() for _ in range(rng.randint(1, 15))) + "/" for _ in range(rng.randint(1, 80))]
if kind == "hidden" and k == 1:
    lines = ["/W/", "/X/", "/" + "X" * 64 + "/", "/HH/HH/HH/", "/QQQ/"]
out("".join(l + "\n" for l in lines) + "*\n")
