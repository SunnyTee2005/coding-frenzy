"""UVa 10409 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    t = s.split()
    i, res = 0, []
    # 用方向向量模擬：記錄每個點數朝哪個方向
    while t[i] != "0":
        n = int(t[i]); cmds = t[i + 1:i + 1 + n]; i += 1 + n
        face = {"up": 1, "n": 2, "w": 3, "down": 6, "s": 5, "e": 4}
        roll = {
            "north": {"up": "n", "n": "down", "down": "s", "s": "up"},
            "south": {"up": "s", "s": "down", "down": "n", "n": "up"},
            "east": {"up": "e", "e": "down", "down": "w", "w": "up"},
            "west": {"up": "w", "w": "down", "down": "e", "e": "up"},
        }
        for c in cmds:
            face = {roll[c].get(d, d): v for d, v in face.items()}
        res.append(str(face["up"]))
    return "\n".join(res) + "\n"
