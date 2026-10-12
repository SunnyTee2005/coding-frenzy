// 英漢字典（考生功能選單）。字典資料尚未收錄，先提供視窗外框與說明。
// TODO：收錄離線英漢字典（例如 ECDICT 的常用字子集，MIT 授權）。

import { useState } from 'react'
import { Window } from '../winforms/Window'

export function DictionaryWindow() {
  const [word, setWord] = useState('')
  return (
    <Window title="英漢字典">
      <div style={{ padding: 10, display: 'flex', gap: 6 }}>
        <input className="wf-textbox" style={{ flex: 1 }} value={word} onChange={(e) => setWord(e.target.value)} placeholder="輸入英文單字" autoFocus />
        <button className="wf-button">查詢</button>
      </div>
      <div className="ie-page" style={{ margin: '0 10px 10px', border: '1px solid #aaa', padding: 10, fontSize: 14 }}>
        <div className="sim-box" style={{ margin: 0 }}>
          <b>【模擬器】</b>離線字典資料尚未收錄。考場的英漢字典無法直接複製貼上題目中的單字，需要自行輸入。
        </div>
      </div>
    </Window>
  )
}
