"""UVa 10415 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10415-{kind}-{k}")
out = sys.stdout.write

songs = ["".join(rng.choice("cdefgabCDEFGAB") for _ in range(rng.randint(0, 200))) for _ in range(rng.randint(1, 80))]
if kind == "hidden" and k == 1:
    songs = ["", "c", "cc", "C", "", "bC", "Cb"]
out(f"{len(songs)}\n" + "".join(s + "\n" for s in songs))
