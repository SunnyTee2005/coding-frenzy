"""UVa 10415 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def r(a, b):
    return set(range(a, b + 1))

FINGERS = {
    "c": r(2, 4) | r(7, 10), "d": r(2, 4) | r(7, 9), "e": r(2, 4) | {7, 8}, "f": r(2, 4) | {7}, "g": r(2, 4), "a": {2, 3}, "b": {2},
    "C": {3}, "D": r(1, 4) | r(7, 9), "E": r(1, 4) | {7, 8}, "F": r(1, 4) | {7}, "G": r(1, 4), "A": r(1, 3), "B": {1, 2},
}

def solve(s: str) -> str:
    lines = s.split("\n")
    res = []
    for song in lines[1:1 + int(lines[0])]:
        cnt = [0] * 11
        prev = set()
        for note in song:
            for f in FINGERS[note] - prev:
                cnt[f] += 1
            prev = FINGERS[note]
        res.append(" ".join(map(str, cnt[1:])))
    return "\n".join(res) + "\n"
