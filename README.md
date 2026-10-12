# CPE 模擬考場（非官方）

在 **Mac**（之後也支援 Windows）上模擬 CPE 大學程式能力檢定的考試環境：使用和考場相同的流程、相同的評判結果字串、ICPC 計分，搭配 CPE26 選集、歷屆考古題與自製測資。

> 本專案與 CPE 委員會、中山大學、瘋狂程設（CodingFrenzy）作者無關。題目直接顯示 UVa 原文 PDF（執行時從公開網址下載），原題版權屬 UVa Online Judge；測資為自製。

## 目前進度

- [x] 判題核心（`crates/judge`）：CCPP（C/C++，和考場一樣都用 g++ 以 C++ 編譯）與 Python；結果字串與考場相同（CORRECT、WRONG-ANSWER、PRESENTATION-ERROR、COMPILER-ERROR、RUN-ERROR、NO-OUTPUT、TIMELIMIT）
- [x] Tauri 桌面 App 骨架，以及環境檢查畫面（Mac 會自動引導安裝 Xcode Command Line Tools）
- [x] ICPC 計分與抽題邏輯
- [x] Phase 0：依官方考生手冊截圖與瘋狂程設套件整理畫面規格（[docs/ui-spec.md](docs/ui-spec.md)、[docs/research.md](docs/research.md)）
- [x] 仿真考場畫面：授權 → 登入 → 題目列表、解題視窗（全部選單與快捷鍵、Dock 版面、建置測試面板、批改確認）、聯賽成績表
- [x] 考試狀態：3 小時倒數、ICPC 計分與罰時、草稿自動存檔、封卷存檔 / 另存新檔 / 提檔續答、結束後的成績報告（含 PR 估算）
- [x] 練習區：CPE26 選集、歷屆考古題（可整場重考）、出題趨勢與預測模擬卷，碼錶計時、不計分
- [x] 題文和考場一樣直接顯示 UVa 原文 PDF（第一次開題時下載並快取，不打包、不放進 repo）
- [x] 題庫 188 題：CPE26 選集 51 / 56 題、近十年考古題 164 題（前三題 114 / 117），6 場 2023 年後的考試可以整場重考（詳見 [docs/research.md](docs/research.md) 的「題庫收錄狀況」）
- [ ] Mac 安裝腳本 / Homebrew、Windows 版

## 開發

需要：Rust（stable）、Node.js 22、C/C++ 編譯器、python3。Mac 只要安裝 Xcode Command Line Tools 就有編譯器和 python3。

```sh
cd app && npm install
npm run tauri dev          # 啟動桌面 App
npm run dev                # 只開前端（瀏覽器，使用 mock 判題）
npm test                   # 前端單元測試

cargo test -p cpe-judge                          # 判題核心測試
cargo run -p cpe-judge -- toolchains             # 列出偵測到的編譯器
cargo run -p cpe-judge -- verify problems        # 用標準解驗證所有題目的測資
python3 tools/build_tests.py [題號...]           # 用 gen.py + sol.cpp 重新產生測資
```

## 專案結構

```
crates/judge/        判題核心（不依賴 Tauri）+ cpe-judge 命令列工具
  languages.toml     語言設定表（新增語言只要加一筆）
  shim/bits/         給 Mac clang 用的 bits/stdc++.h
app/                 Tauri 2 + React 前端
  src-tauri/         Rust 後端 command
problems/uva-*/      題庫：meta.toml、sample/、public/、hidden/、sol.cpp、gen.py（題文用 UVa 原文 PDF）
data/                歷屆考題（history.json）與題型標籤（tags.json）
tools/               測資產生（build_tests.py、problem_kit.py）、交叉驗證（crosscheck/）、考古題抓取（fetch_history.py）
docs/research.md     考場環境研究筆記、題庫清單、成績分布
docs/ui-spec.md      考場畫面規格（版面、選單、快捷鍵、對話框）
```

## 題目格式

| 目錄 / 檔案 | 用途 | 列入成績 |
|---|---|---|
| `sample/` | 題目預設測試資料（題目上的範例） | 否 |
| `public/` | 人工公開測試資料 | 否 |
| `hidden/` | 暗中測試資料，正式評判用 | 是 |
| `gen.py` | `python3 gen.py <public\|hidden> <編號>` 輸出一筆測資的輸入 | — |
| `sol.cpp` | 標準解，用來產生答案與驗證測資 | — |
