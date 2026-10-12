# CPE 模擬考場（非官方）

在 **Mac**（之後也支援 Windows）上模擬 CPE 大學程式能力檢定的考試環境：使用和考場相同的流程、相同的評判結果字串、ICPC 計分，搭配一顆星選集題庫與自製測資。

> 本專案與 CPE 委員會、中山大學、瘋狂程設（CodingFrenzy）作者無關。題目敘述為自行改寫，原題版權屬 UVa Online Judge。

## 目前進度

- [x] 判題核心（`crates/judge`）：C / C++ / Python 3；可判 CORRECT、WRONG-ANSWER、PRESENTATION-ERROR、COMPILER-ERROR、RUN-ERROR、NO-OUTPUT、逾時
- [x] Tauri 桌面 App 骨架，以及環境檢查畫面（Mac 會自動引導安裝 Xcode Command Line Tools）
- [x] ICPC 計分與抽題邏輯
- [ ] Phase 0：取得原考場軟體的 UI 規格（見 [docs/research.md](docs/research.md)）
- [ ] 仿真考場畫面
- [ ] 一顆星 49 題題庫（目前只有範例題 UVa 10055）
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
problems/uva-*/      題庫：meta.toml、statement.md、sample/、public/、hidden/、sol.cpp、gen.py
tools/               測資產生工具
docs/research.md     考場環境研究筆記與待確認清單
```

## 題目格式

| 目錄 / 檔案 | 用途 | 列入成績 |
|---|---|---|
| `sample/` | 題目預設測試資料（題目上的範例） | 否 |
| `public/` | 人工公開測試資料 | 否 |
| `hidden/` | 暗中測試資料，正式評判用 | 是 |
| `gen.py` | `python3 gen.py <public\|hidden> <編號>` 輸出一筆測資的輸入 | — |
| `sol.cpp` | 標準解，用來產生答案與驗證測資 | — |
