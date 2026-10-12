"""UVa 10258 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


def solve(s: str) -> str:
    blocks = s.split("\n\n")[1:]
    outs = []
    for b in blocks:
        state = {}
        for line in b.splitlines():
            if not line.strip():
                continue
            who, prob, time, L = line.split()
            who, prob, time = int(who), int(prob), int(time)
            st = state.setdefault(who, {"done": set(), "wrong": {}, "n": 0, "pen": 0})
            if prob in st["done"]:
                continue
            if L == "C":
                st["done"].add(prob); st["n"] += 1; st["pen"] += time + 20 * st["wrong"].get(prob, 0)
            elif L == "I":
                st["wrong"][prob] = st["wrong"].get(prob, 0) + 1
        rows = sorted(state.items(), key=lambda kv: (-kv[1]["n"], kv[1]["pen"], kv[0]))
        outs.append("".join(f"{w} {st['n']} {st['pen']}\n" for w, st in rows))
    return "\n".join(outs)
