"""UVa 828 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"828-{kind}-{k}")
out = sys.stdout.write

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def ciph(ch, n):
    return A[(A.index(ch) + n) % 26]
def decodings(msg, L, n):
    # 所有可能的明文（數量上限 2）
    inL = set(L)
    found = []
    def go(i, m, acc):
        if len(found) >= 2:
            return
        if i == len(msg):
            found.append(acc); return
        ch = msg[i]
        if ch == " ":
            go(i + 1, m, acc + " "); return
        p = A[(A.index(ch) - n) % 26]
        if p not in inL:
            go(i + 1, m, acc + p)
        if ch == L[m % len(L)] and i + 2 < len(msg) and msg[i + 1] != " " and msg[i + 2] == L[(m + 1) % len(L)]:
            p = A[(A.index(msg[i + 1]) - n) % 26]
            if p in inL:
                go(i + 3, m + 1, acc + p)
    go(0, 0, "")
    return found
def greedy(msg, L, n):
    out, m, i = [], 0, 0
    while i < len(msg):
        ch = msg[i]
        if ch == " ":
            out.append(" "); i += 1; continue
        if ch == L[m % len(L)] and i + 2 < len(msg) and msg[i + 1] != " " and msg[i + 2] == L[(m + 1) % len(L)] \
                and A[(A.index(msg[i + 1]) - n) % 26] in L:
            out.append(A[(A.index(msg[i + 1]) - n) % 26]); m += 1; i += 3
        else:
            p = A[(A.index(ch) - n) % 26]
            if p in L:
                return None
            out.append(p); i += 1
    return "".join(out)
def encrypt(plain, L, n):
    out, m = [], 0
    for ch in plain:
        if ch == " ":
            out.append(" ")
        elif ch in L:
            out.append(L[m % len(L)] + ciph(ch, n) + L[(m + 1) % len(L)]); m += 1
        else:
            out.append(ciph(ch, n))
    return "".join(out)
cases = []
for _ in range(rng.randint(1, 3)):
    while True:
        n = rng.randint(1, 25)
        L = "".join(rng.sample(A, rng.randint(1, 8)))
        if not any(ciph(x, n) in L for x in L):  # 題目保證 ciph(L) 與 L 不相交
            break
    msgs = []
    tries = 0
    while len(msgs) < rng.randint(1, 10) and tries < 400:
        tries += 1
        words = ["".join(rng.choice(L + A if rng.random() < 0.5 else A) for _ in range(rng.randint(1, 6))) for _ in range(rng.randint(1, 4))]
        msg = encrypt(" ".join(words), L, n)
        if rng.random() < 0.4:  # 改壞一個字
            i = rng.randrange(len(msg))
            if msg[i] != " ":
                msg = msg[:i] + rng.choice(A) + msg[i + 1:]
        ds = decodings(msg, L, n)
        # 只出能唯一解密或無法解密的訊息，而且「能套規則 3 就套」的直覺解法也要得到同樣結果
        if len(ds) <= 1 and greedy(msg, L, n) == (ds[0] if ds else None):
            msgs.append(msg)
    if msgs:
        cases.append((L, n, msgs))
if not cases:
    cases = [("RSAEIO", 2, ["RGSSCAV"])]
out(f"{len(cases)}\n\n" + "\n".join(f"{L}\n{n}\n{len(ms)}\n" + "".join(m + "\n" for m in ms) for L, n, ms in cases))
