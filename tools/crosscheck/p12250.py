"""UVa 12250 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


LANG = dict(HELLO="ENGLISH", HOLA="SPANISH", HALLO="GERMAN", BONJOUR="FRENCH", CIAO="ITALIAN", ZDRAVSTVUJTE="RUSSIAN")

def solve(s: str) -> str:
    res = []
    for i, w in enumerate(s.split()):
        if w == "#":
            break
        res.append(f"Case {i + 1}: {LANG.get(w, 'UNKNOWN')}")
    return "\n".join(res) + "\n"
