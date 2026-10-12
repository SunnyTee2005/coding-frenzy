#!/usr/bin/env python3
"""下載 CPE 官方「歷次考題一覽」，整理成 data/history.json。

來源：https://cpe.mcu.edu.tw/cpe/test_data/problems（中山大學 CPE 官網的銘傳鏡像）
內容是公開的考試統計：每場的日期、平均答對題數，以及每一題的 UVa 編號、題名與答對率。

用法：python3 tools/fetch_history.py [已下載的 HTML 檔]
"""
import html
import json
import pathlib
import re
import sys
import urllib.request

URL = "https://cpe.mcu.edu.tw/cpe/test_data/problems"
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "history.json"

# 官方清單偶有「題名與 UVa 編號對不上」的情形。以編號為準（題目 PDF 依編號提供），
# 這裡記錄該編號實際的 UVa 題名；已用 CPE 鏡像上的 PDF 或 UVa 題庫核對。
UVA_TITLE_FIX = {
    10405: "Longest Common Subsequence",  # 官方列為 Jolly Jumpers（UVa 10038）
    10635: "Prince and Princess",  # 官方列為 The Art Gallery
    10740: "Not the Best",  # 官方列為 First Love!!!
    10935: "Throwing cards away I",  # 官方列為 Even Parity（UVa 11464）
    11219: "How old are you?",  # 官方列為 Basic wall maze
    10436: "Cheapest way",  # 官方列為 Dog and Gopher（UVa 10310）
    10903: "Rock-Paper-Scissors Tournament",  # 官方列為 Playing War
    11000: "Bee",  # 官方列為 The Four in One Stadium
    11764: "Jumping Mario",  # 官方列為 Cricket Field
}


def fetch() -> str:
    if len(sys.argv) > 1:
        return pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    req = urllib.request.Request(URL, headers={"User-Agent": "cpe-sim history fetcher"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def num(s: str):
    s = s.strip().rstrip("%")
    return float(s) if "." in s else int(s)


def parse(page: str) -> list[dict]:
    # 頁面裡有被註解掉的舊連結與舊欄位，先拿掉
    page = re.sub(r"(?s)<!--.*?-->", "", page)
    exams = {}
    for table in re.split(r"<table\b", page)[1:]:
        head = re.search(r"(\d{4}-\d{2}-\d{2}) CPE\s*\(\s*_?平均答對題數：([\d.]+)\)", table)
        if not head:
            continue
        date, avg = head.group(1), float(head.group(2))
        problems = []
        for row in re.findall(r"(?s)<tr>(.*?)</tr>", table):
            m = re.search(r'problemPdf/(\d+)\.pdf">\s*(\d+):\s*(.*?)\s*</a>', row)
            if not m:
                continue
            cells = re.findall(r"<td><center>\s*([\d.]+%?)\s*</center></td>", row)
            if len(cells) < 6:
                continue
            a, b, c, d, e, f = (num(x) for x in cells[:6])
            problems.append(
                {
                    "pos": len(problems) + 1,
                    "uva": int(m.group(2)),
                    "title": html.unescape(m.group(3)).strip(),
                    "uvaTitle": UVA_TITLE_FIX.get(int(m.group(2))),
                    "submissions": a,
                    "attempted": b,
                    "solved": c,
                    "rateSubmit": d,
                    "rateAttempt": e,
                    "rateAll": f,
                }
            )
        if problems and date not in exams:
            exams[date] = {"date": date, "avgSolved": avg, "problems": problems}
    return sorted(exams.values(), key=lambda x: x["date"])


def main():
    exams = parse(fetch())
    if not exams:
        sys.exit("沒有解析到任何考試，頁面格式可能改了")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(exams, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    slots = sum(len(e["problems"]) for e in exams)
    print(f"{len(exams)} 場考試（{exams[0]['date']} ~ {exams[-1]['date']}），共 {slots} 題次 → {OUT}")


if __name__ == "__main__":
    main()
