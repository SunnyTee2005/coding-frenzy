"""UVa 441 的獨立解法（與 sol.cpp 分開撰寫，用來交叉驗證測資答案）。"""


from itertools import combinations

def solve(s: str) -> str:
    it = iter(map(int, s.split()))
    blocks = []
    for k in it:
        if k == 0:
            break
        nums = [next(it) for _ in range(k)]
        blocks.append("".join(" ".join(map(str, c)) + "\n" for c in combinations(nums, 6)))
    return "\n".join(blocks)
