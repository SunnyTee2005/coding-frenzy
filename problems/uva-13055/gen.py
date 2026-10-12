"""UVa 13055 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"13055-{kind}-{k}")
out = sys.stdout.write

def name():
    return "".join(rng.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(rng.randint(1, 15)))
n = rng.randint(1, 10000 if k == 10 else 600)
ops = []
for _ in range(n):
    r = rng.random()
    ops.append(f"Sleep {name()}" if r < 0.4 else ("Kick" if r < 0.7 else "Test"))
if kind == "hidden" and k == 1:
    ops = ["Test", "Kick", "Kick", "Test", "Sleep a", "Kick", "Kick", "Test", "Sleep ABCDEFGHIJKLMNO", "Test"]
out(f"{len(ops)}\n" + "".join(o + "\n" for o in ops))
