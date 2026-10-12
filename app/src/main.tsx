import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './winforms/winforms.css'
import './screens/iepage.css'
import { DialogHost } from './winforms/Dialogs'
import { MainWindow } from './screens/MainWindow'
import { SolveWindow } from './screens/SolveWindow'
import { Scoreboard } from './screens/Scoreboard'
import { PracticeWindow } from './screens/Practice'
import type { Mode } from './judge/types'

// 每個 Tauri 視窗載入同一個頁面，用 hash 決定要顯示什麼：
//   #/                         主畫面（授權 → 登入 → 題目列表）
//   #/solve/{exam|practice|view}/{題號}  解題視窗（view 為「看題」）
//   #/scoreboard  #/practice
function route() {
  const parts = location.hash.replace(/^#\/?/, '').split('/')
  switch (parts[0]) {
    case 'solve':
      return <SolveWindow mode={parts[1] as Mode | 'view'} problemId={parts[2]} />
    case 'scoreboard':
      return <Scoreboard />
    case 'practice':
      return <PracticeWindow />
    default:
      return <MainWindow />
  }
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <DialogHost>{route()}</DialogHost>
  </StrictMode>,
)
