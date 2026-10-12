"""UVa 10420 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10420-{kind}-{k}")
out = sys.stdout.write

C = ["Spain", "England", "Italy", "Germany", "France", "Turkey", "Taiwan", "Japan", "Brazil", "spain", "USA", "Z", "A"]
NAMES = ["Donna Elvira", "Donna Anna", "Jane Doe", "Zerlina", "Mary Ann Lee", "X"]
n = rng.randint(1, 1999 if k == 10 else 100)
pool = rng.sample(C, rng.randint(1, len(C)))
out(f"{n}\n" + "".join(f"{rng.choice(pool)} {rng.choice(NAMES)}\n" for _ in range(n)))
