#!/bin/bash
# 新增題目後的完整檢查：產生測資 → 標準解驗證（含大小上限）→ 獨立解法交叉比對
# 用法：tools/check_new.sh <題號...>
set -e
cd "$(dirname "$0")/.."
python3 tools/build_tests.py "$@" 2>/dev/null
cargo run -q -p cpe-judge -- verify problems "$@"
python3 tools/crosscheck/run.py "$@"
