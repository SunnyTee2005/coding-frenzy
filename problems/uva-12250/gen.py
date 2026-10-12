"""UVa 12250 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"12250-{kind}-{k}")
out = sys.stdout.write

W = ["HELLO", "HOLA", "HALLO", "BONJOUR", "CIAO", "ZDRAVSTVUJTE", "HELO", "HELLOO", "ABC", "CIA", "BONJOURS", "HI", "Z"]
ws = [rng.choice(W) for _ in range(rng.randint(1, 500))]
out("".join(w + "\n" for w in ws) + "#\n")
