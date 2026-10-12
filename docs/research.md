# CPE 考試環境研究筆記

> 本專案是**非官方**的 CPE 模擬考試環境，與 CPE 委員會、中山大學、瘋狂程設作者均無關。
> repo 內不放官方程式、反編譯原始碼或官方截圖；這份文件只記錄觀察結果。
> 參考資料（官方 PDF、原程式、截圖）請放在本機的 `research/`（已列入 .gitignore）。

## 1. 考場軟體：瘋狂程設 CodingFrenzy（CodingFrenzy@CPExam）

- 自 2013/10/1 起，CPE 改用「瘋狂程設」評判系統。作者是阿平（coding-frenzy.arping.me）。
- **只支援 Windows**，依賴 Microsoft .NET Framework 2.0（WinForms）。
- 考生機安裝方式：下載 `CodingFrenzy@CPExam.zip`，解壓到 `C:\CodingFrenzy@CPExam`，執行 `CodingFrenzy.exe`。
- 編譯器要另外安裝，而且必須在**預設路徑**，瘋狂程設才會自動抓到；改路徑就找不到。CPE 官網的協辦專區有自動安裝程序檔。
- 練習時用「瘋狂程設帳號」，正式考試用「CPE 帳號」，兩者不同。

### 考場語言（environment.php，2021/10 安裝包）

| 語言 | 版本 |
|---|---|
| C/C++ | MinGW GCC 6.3.0 |
| C/C++ | MSVC v140 |
| Java | AdoptOpenJDK 8、AdoptOpenJDK 11 |
| Python | Python 3.9.6 |

硬體需求：19 吋以上螢幕、雙核 2GHz、4GB RAM、Windows 7 以上。

## 2. 考試流程（考生視角）

1. 啟動程式 → **同意授權規定** → 連線到伺服器（伺服器依考生簽到表分配）。
2. **登入**：輸入身分證字號、准考證號碼。
3. 主畫面：**考生功能**、**現在時間**、**考試題目列表**。
4. 題目列表每題有 **「看題」** 和 **「解題」** 兩個按鈕。看題不計時；按「解題」後題目才開啟、開始計時（考生心得的說法）。
5. 解題視窗（綜合多篇描述，待 Phase 0 以原程式確認）：
   - 最上方是**工具列**。
   - 最左邊是 **「批改交卷」**，也就是正式評判，按下會跳出確認視窗。
   - 右側有三個測試按鈕：**題目預設測試資料**、**自訂測試資料**、**人工公開測試資料**。
   - 中間是題目，題目下方寫程式。
   - 右半部顯示編譯結果與範例輸入輸出。
   - 快捷鍵：**Alt+L** 選擇編譯器，**Alt+J** 觀看評判結果。
   - 編譯器選單的項目字串例如 `CCPP:MinGW`。
6. 三種測試都**不列入成績**：
   - 題目預設測試資料：系統產生，難度較低。
   - 自訂測試資料：考生自行輸入。
   - 人工公開測試資料。
7. **正式評判**用不公開的「暗中測試資料」，結果列入正式紀錄，並顯示在所有考生的成績表上。
8. 結果狀態：`CORRECT`、`WRONG-ANSWER`、`PRESENTATION-ERROR`、`COMPILER-ERROR`（點連結可看編譯器錯誤訊息）、`RUN-ERROR`、`NO-OUTPUT`，以及等待中。
9. **考生功能**：成績表（觀看所有考生正式考題的成績）、考生手冊（考生機桌面「考生功能\考生手冊」）。
10. 有**線上字典**可查英文單字（考生心得）。

## 3. 考試規則

- 7 題：3 題一顆星、2 題二顆星、1 題三顆星、1 題四顆星。題目來自 UVa Online Judge。
- 考試時間 3 小時，例如 18:40–21:40，19:40 後可離場。
- **計分採 ICPC 制**：
  - 先比答對題數，同題數再比解題時間總和。
  - 每題的時間 = 從開考到答對的分鐘數 + 每次錯誤提交 × 20 分鐘。
  - 沒答對的題目不計時間與罰時。
  - 官方範例：10 分答對 A；15 分 B 錯誤、32 分答對 B → 10 + 32 + 20×1 = 62。
- 成績報告有兩種成績：「絕對成績」依答對題數分級，「相對成績」依 ICPC 排名。成果報告中有各題數的累計百分比。

## 4. 待確認清單（Phase 0，需在 local session 取得官方資料）

資料來源：
- 考生使用手冊：`CPE_manual_231128.pdf`、`CPE_manual.pdf`（2022/9）、`CPE_manual_en.pdf`（2018/5）
- 連線測試流程：`frenzy_testing231203.pdf`
- 環境頁：`environment.php`
- 成果報告：`CPE_report_*.pdf`
- 原程式：`CodingFrenzy@CPExam.zip`，用 `ilspycmd` 反編譯

逐項確認：

- [ ] 每個視窗的 ClientSize、控制項 Location/Size/Text/Font、選單結構（反編譯 `*.Designer.cs` → `docs/ui-spec/*.json`）
- [ ] 所有 MessageBox 的標題、內文與按鈕（授權規定、登入失敗、批改交卷確認、時間到……）
- [ ] 編譯器選單的完整字串清單，以及各編譯器實際的編譯 / 執行指令與參數
- [ ] 逾時的狀態字串（目前暫用 `TIME-LIMIT-EXCEEDED`）、記憶體限制與對應狀態
- [ ] 輸出比對規則：行尾空白、檔尾換行、CRLF 的處理方式，以及 PE 的判定方式
- [ ] Python 語法錯誤顯示為 COMPILER-ERROR 還是 RUN-ERROR
- [ ] 計時起點：從開考算，還是從按「解題」算？COMPILER-ERROR 是否罰時？
- [ ] 預設時限
- [ ] 「題目預設測試資料（系統產生）」和題目上的 Sample 是否相同
- [ ] 成績表的欄位與排序；現在時間 / 剩餘時間的顯示格式
- [ ] 線上字典的形式（內建視窗，還是開瀏覽器）
- [ ] 視窗字型（新細明體 / 微軟正黑體？）、配色、圖示風格
- [ ] 一顆星選集 49 題清單；歷屆考題的星等分布
- [ ] 成果報告中各題數的累計百分比（用來估算 PR 值）

## 參考來源

- [CPE 官網（中山大學）](https://cpe.cse.nsysu.edu.tw/)、[環境頁](https://cpe.cse.nsysu.edu.tw/environment.php)
- [考生使用手冊 2023/11](https://cpe.mcu.edu.tw/doc/CPE_manual_231128.pdf)、[英文手冊 2018](https://cpe.cse.nsysu.edu.tw/doc/CPE_manual_en.pdf)
- [瘋狂程設連線測試流程 2023/12](https://cpe.mcu.edu.tw/doc/frenzy_testing231203.pdf)
- [CPE 考試當天流程](https://cpe.cse.nsysu.edu.tw/doc/CPE_examsop.pdf)、[CPE 簡介（楊昌彪）](https://nur.asia.edu.tw/uploads/asset/data/607f9288905fc3c8cc00002a/CPE_introduction.pdf)
- [CPE 成果報告 2022/3](https://cpe.cse.nsysu.edu.tw/doc/CPE_report_220322.pdf)
- [瘋狂程設官網](https://coding-frenzy.arping.me/)、[阿平雜記：瘋狂程設系列網站使用方式](http://arpingme.blogspot.com/2013/11/blog-post.html)
- [NIU CSIE：CPE 瘋狂程設安裝設定教學](https://sescies.github.io/1129359603876068/2017/04/05/CPE%E7%98%8B%E7%8B%82%E7%A8%8B%E8%A8%AD%E5%AE%89%E8%A3%9D%E8%A8%AD%E5%AE%9A%E6%95%99%E5%AD%B8(%E5%90%AB%E7%B7%A8%E8%AD%AF%E5%99%A8).html)
- [巴哈姆特：瘋狂程設題目 UVA10035](https://home.gamer.com.tw/creationDetail.php?sn=2901057)、[CPE 心得（Kola）](https://cozy-kola.medium.com/cpe%E5%BF%83%E5%BE%97-%E6%8C%81%E7%BA%8C%E6%9B%B4%E6%96%B0%E4%B8%AD-1f8a07bdcbeb)
- [CPE 一顆星選集 49 題](https://yuihuang.com/cpe-level-1-49/)
