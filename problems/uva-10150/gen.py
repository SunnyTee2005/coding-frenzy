"""UVa 10150 測資：python3 gen.py <public|hidden> <編號>，輸入寫到 stdout。"""
import random
import sys

kind, k = sys.argv[1], int(sys.argv[2])
rng = random.Random(f"10150-{kind}-{k}")
out = sys.stdout.write

# 題目允許輸出任一條最短路徑；為了能逐字比對，只出最短路徑唯一（或無解）的詢問
from collections import deque
def nb(w, words):
    return [x for x in words if len(x) == len(w) and sum(a != b for a, b in zip(w, x)) == 1]
def paths(a, b, words):
    dist, cnt = {a: 0}, {a: 1}
    q = deque([a])
    while q:
        u = q.popleft()
        for v in nb(u, words):
            if v not in dist:
                dist[v] = dist[u] + 1; cnt[v] = cnt[u]; q.append(v)
            elif dist[v] == dist[u] + 1:
                cnt[v] += cnt[u]
    return cnt.get(b, 0)
L = rng.randint(3, 5)
al = "abcde"[:rng.randint(2, 4)]
words = sorted({"".join(rng.choice(al) for _ in range(rng.choice([L, L, L, L - 1]))) for _ in range(rng.randint(5, 60))})
rng.shuffle(words)
pairs = []
tries = 0
while len(pairs) < rng.randint(1, 12) and tries < 500:
    tries += 1
    a, b = rng.choice(words), rng.choice(words)
    if a != b and paths(a, b, set(words)) <= 1:
        pairs.append((a, b))
if not pairs:
    pairs = [(words[0], words[-1])] if words[0] != words[-1] and paths(words[0], words[-1], set(words)) <= 1 else []
if not pairs:
    words, pairs = ["abc", "abd", "xyz"], [("abc", "abd"), ("abc", "xyz")]
out("".join(w + "\n" for w in words) + "\n" + "".join(f"{a} {b}\n" for a, b in pairs))
