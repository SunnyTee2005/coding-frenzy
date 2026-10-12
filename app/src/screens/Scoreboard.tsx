// 成績表（聯賽成績）。依圖 1.2.4：每題「次數(分鐘+罰時)」，答對綠底、答錯粉紅、未交米白。
// 考場的成績表每 5 分鐘更新一次，這裡照做（也可以按「更新(R)」）。

import { useCallback, useEffect, useState } from 'react'
import { api } from '../judge/api'
import type { ProblemMeta, Session } from '../judge/types'
import { scoreExam, PENALTY_MINUTES } from '../exam/scoring'
import { formatMonthDayHms, problemCode } from '../exam/session'
import { Window } from '../winforms/Window'
import { MenuBar } from '../winforms/MenuBar'

const REFRESH_MS = 5 * 60 * 1000

export function Scoreboard() {
  const [snapshot, setSnapshot] = useState<{ session: Session; at: number } | null>(null)
  const [bank, setBank] = useState<ProblemMeta[]>([])

  const refresh = useCallback(() => {
    api.sessionGet().then((v) => setSnapshot({ session: v.session, at: v.nowMs }))
  }, [])

  useEffect(() => {
    refresh()
    api.problems().then(setBank)
    const t = setInterval(refresh, REFRESH_MS)
    return () => clearInterval(t)
  }, [refresh])

  const menus = [
    { label: '上一頁', mnemonic: 'B', disabled: true },
    { label: '下一頁', mnemonic: 'N', disabled: true },
    { label: '更新', mnemonic: 'R', onSelect: refresh },
    { label: '搜尋', mnemonic: 'S', disabled: true },
    { label: '搜尋下一個', mnemonic: 'D', disabled: true },
  ]

  const exam = snapshot?.session.exam ?? null
  const e = snapshot?.session.examinee ?? null

  return (
    <Window title="聯賽成績(限網：模擬考場)">
      <MenuBar menus={menus} />
      <div className="ie-page" style={{ fontFamily: 'var(--wf-font)', fontSize: 12 }}>
        <div style={{ background: '#5a5a5a', color: '#fff', fontWeight: 'bold', padding: '3px 6px' }}>
          (點選標題可排序) 這是來自 <span style={{ color: '#ffb6c1' }}>模擬考場</span> 分站 於{' '}
          <span style={{ color: '#ffb6c1' }}>{snapshot ? formatMonthDayHms(snapshot.at) : ''}</span> 的整合性資料。 本表{' '}
          <span style={{ color: '#ffb6c1' }}>5分鐘</span> 內會更新一次，請耐心等待!! 必要時 請更新瀏覽一次。
        </div>
        {!exam || !e ? (
          <div style={{ padding: 12 }}>尚未開始考試。</div>
        ) : (
          <ScoreTable session={snapshot!.session} bank={bank} />
        )}
      </div>
    </Window>
  )
}

function ScoreTable({ session, bank }: { session: Session; bank: ProblemMeta[] }) {
  const exam = session.exam!
  const e = session.examinee!
  const ids = exam.problems.map((p) => p.problemId)
  const score = scoreExam(ids, exam.submissions)

  const head: React.CSSProperties = { background: 'linear-gradient(#ffe48a, #f7c430)', border: '1px solid #c9a23a', padding: '3px 6px', whiteSpace: 'nowrap' }
  const cell: React.CSSProperties = { border: '1px solid #d8c9a0', padding: '3px 6px', whiteSpace: 'nowrap' }
  const filterRow = <input className="wf-textbox" style={{ width: '100%', height: 18 }} disabled />

  return (
    <table style={{ borderCollapse: 'collapse', margin: 2, background: '#fffaf0' }}>
      <thead>
        <tr>
          {['序', '學校', '暱稱', '解題', '耗時'].map((h) => (
            <th key={h} style={head}>
              {h}
            </th>
          ))}
          {exam.problems.map((p) => (
            <th key={p.label} style={head}>
              {problemCode(p.label, bank.find((b) => b.id === p.problemId)?.uva ?? null, p.problemId)}
            </th>
          ))}
          {['身分證', '複准', '准考碼-認證碼'].map((h) => (
            <th key={h} style={head}>
              {h}
            </th>
          ))}
        </tr>
        <tr>
          {Array.from({ length: 8 + exam.problems.length }, (_, i) => (
            <td key={i} style={{ ...cell, background: '#fff3c4' }}>
              {filterRow}
            </td>
          ))}
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style={{ ...cell, textAlign: 'right' }}>1</td>
          <td style={cell}>模擬考場</td>
          <td style={cell}>{e.name}</td>
          <td style={cell}>{score.solved}題</td>
          <td style={cell}>{score.totalTime}分</td>
          {score.problems.map((p) => {
            const attempts = p.solved ? p.wrongAttempts + 1 : p.wrongAttempts
            const bg = p.solved ? '#90ee90' : p.wrongAttempts ? '#ffc0cb' : '#fff8e7'
            return (
              <td key={p.problemId} style={{ ...cell, background: bg, textAlign: 'center' }}>
                <b>{attempts}</b>
                <small>
                  ( {p.solvedAt ?? 0}+{p.wrongAttempts * PENALTY_MINUTES})
                </small>
              </td>
            )
          })}
          <td style={{ ...cell, textAlign: 'center' }}>{e.idNo.slice(-3)}</td>
          <td style={cell} />
          <td style={cell}>
            {e.ticket}-{e.authCode}
          </td>
        </tr>
      </tbody>
    </table>
  )
}
