"""UVa 1062 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"1062-{kind}-{k}")
out = sys.stdout.write

ss = []
for _ in range(rng.randint(1, 60)):
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:rng.randint(1, 26)]
    ss.append("".join(rng.choice(al) for _ in range(rng.randint(1, 1000 if k == 10 else 60))))
if kind == "hidden" and k == 1:
    ss = ["A", "Z", "AZ", "ZA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZYXWVUTSRQPONMLKJIHGFEDCBA", "AAAA"]
out("".join(x + "\n" for x in ss) + "end\n")
