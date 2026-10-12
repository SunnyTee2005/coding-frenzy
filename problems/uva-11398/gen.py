"""UVa 11398 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"11398-{kind}-{k}")
out = sys.stdout.write

def encode(bits):
    toks, flag = [], None
    i = 0
    while i < len(bits):
        b = bits[i]
        j = i
        while j < len(bits) and bits[j] == b and j - i < 5:
            j += 1
        toks.append("0" if b == "1" else "00")
        toks.append("0" * (j - i + 2))
        i = j
    return " ".join(toks) + " #"
nums = [rng.randint(1, 2**30 - 1) for _ in range(rng.randint(3, 40))]
if kind == "hidden" and k == 1:
    nums = [1, 2, 3, 4, 5, 2**30 - 1, 2**29, 6]
out("".join(encode(bin(x)[2:]) + "\n" for x in nums) + "~\n")
