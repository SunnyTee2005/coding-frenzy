"""UVa 948 測資：python3 gen.py <public|hidden> <編號>"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"948-{kind}-{k}")
LIMIT = 99_999_999

fib = [1, 2]
while fib[-1] <= LIMIT:
    fib.append(fib[-1] + fib[-2])

if kind == "hidden" and k == 1:
    xs = list(range(1, 60))
elif kind == "hidden" and k == 2:
    # Fibonacci 數本身與前後一個數
    xs = [v + d for v in fib if v <= LIMIT for d in (-1, 0, 1) if 1 <= v + d <= LIMIT] + [LIMIT]
elif kind == "hidden" and k >= 8:
    xs = [rng.randint(1, LIMIT) for _ in range(3000)]
else:
    xs = [rng.randint(1, 10 ** rng.randint(1, 8) - 1) for _ in range(rng.randint(5, 100))]
sys.stdout.write(f"{len(xs)}\n" + "".join(f"{x}\n" for x in xs))
