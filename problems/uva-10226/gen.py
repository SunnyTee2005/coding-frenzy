"""UVa 10226 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10226-{kind}-{k}")
out = sys.stdout.write

TREES = ["Red Alder", "Ash", "Aspen", "Basswood", "Beech", "Yellow Birch", "Cherry", "Cottonwood", "Cypress", "Red Elm",
         "Gum", "Hackberry", "White Oak", "Hickory", "Pecan", "Hard Maple", "Soft Maple", "Red Oak", "Poplan", "Sassafras",
         "Sycamore", "Black Walnut", "Willow", "ash", "Z", "a b"]
cases = []
for _ in range(rng.randint(1, 4)):
    pool = rng.sample(TREES, rng.randint(1, len(TREES)))
    cases.append([rng.choice(pool) for _ in range(rng.randint(1, 300))])
out(f"{len(cases)}\n\n" + "\n".join("".join(x + "\n" for x in c) for c in cases))
