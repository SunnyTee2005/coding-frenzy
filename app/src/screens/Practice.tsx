// 練習區（模擬器額外功能，不是考場畫面）：三個分頁
//   CPE26 選集：自由挑題練習，解題視窗改用碼錶、不計分
//   歷屆考古題：官方歷次考題，可單題練習或整場重考
//   出題趨勢：歷屆統計與下次考試的預測

import { useEffect, useState } from 'react'
import { api } from '../judge/api'
import type { ProblemMeta, Session } from '../judge/types'
import { CPE26 } from '../exam/cpe26'
import { HISTORY } from '../exam/history'
import { useSession } from '../exam/session'
import { Window } from '../winforms/Window'
import { HistoryTab } from './History'
import { TrendsTab } from './Trends'

type Tab = 'cpe26' | 'history' | 'trends'
const TABS: [Tab, string][] = [
  ['cpe26', 'CPE26 選集'],
  ['history', '歷屆考古題'],
  ['trends', '出題趨勢'],
]

export function PracticeWindow() {
  const session = useSession()
  const [bank, setBank] = useState<ProblemMeta[]>([])
  const [tab, setTab] = useState<Tab>('cpe26')
  useEffect(() => {
    api.problems().then(setBank)
  }, [])

  return (
    <Window title="練習區">
      <div className="wf-tabstrip">
        {TABS.map(([key, label]) => (
          <div key={key} className={'wf-tab' + (tab === key ? ' active' : '')} onClick={() => setTab(key)}>
            {label}
          </div>
        ))}
      </div>
      <div className="ie-page" style={{ padding: '10px 14px' }}>
        {tab === 'cpe26' && <Cpe26Tab bank={bank} session={session} />}
        {tab === 'history' && <HistoryTab bank={bank} session={session} />}
        {tab === 'trends' && <TrendsTab bank={bank} />}
      </div>
    </Window>
  )
}

function Cpe26Tab({ bank, session }: { bank: ProblemMeta[]; session: Session | null }) {
  const inBank = new Set(bank.map((p) => p.id))
  const inHistory = new Set(HISTORY.flatMap((e) => e.problems.map((p) => String(p.uva))))
  const extra = bank.filter((p) => !CPE26.some((c) => String(c.uva) === p.id) && !inHistory.has(p.id))
  const solvedCount = CPE26.filter((c) => session?.practice[String(c.uva)]?.solvedAtMs).length

  const row = (id: string, cpe: string, title: string, category: string) => {
    const rec = session?.practice[id]
    return (
      <tr key={id}>
        <td>{category}</td>
        <td>{cpe}</td>
        <td>UVA{id}</td>
        <td>{title}</td>
        <td style={{ textAlign: 'center' }}>{inHistory.has(id) ? '考過' : ''}</td>
        <td style={{ textAlign: 'center' }}>
          {rec?.solvedAtMs ? <b style={{ color: 'red' }}>通過</b> : rec?.attempts ? `嘗試 ${rec.attempts} 次` : ''}
        </td>
        <td>
          {inBank.has(id) ? (
            <a onClick={() => api.openSolveWindow('practice', id, `PRAC.UVA${id}評量:${title}`)}>練習</a>
          ) : (
            <span style={{ color: '#999' }}>尚未收錄</span>
          )}
        </td>
      </tr>
    )
  }

  const head = (cols: string[]) => (
    <thead>
      <tr>
        {cols.map((h) => (
          <th key={h} style={{ border: '1px solid #aaa', background: '#eee', padding: '2px 6px' }}>
            {h}
          </th>
        ))}
      </tr>
    </thead>
  )

  return (
    <>
      <div style={{ fontSize: 14, marginBottom: 8 }}>
        2027 年起，每次 CPE 會有一題選自 CPE26 選集。這裡的解題視窗和考場相同，但計時器改成碼錶、正式評判不計罰時。
        已通過 <b>{solvedCount}</b> / {CPE26.length} 題（收錄 {CPE26.filter((c) => inBank.has(String(c.uva))).length} 題）。
      </div>
      <table className="build-table" style={{ fontSize: 14, width: 'auto' }}>
        {head(['分類', '編號', 'UVa', '題目', '歷屆', '狀態', ''])}
        <tbody>{CPE26.map((c) => row(String(c.uva), `cpe${c.cpe}`, c.title, c.category))}</tbody>
      </table>
      {extra.length > 0 && (
        <>
          <h2 style={{ fontSize: 18, marginTop: 20 }}>其他收錄題目</h2>
          <table className="build-table" style={{ fontSize: 14, width: 'auto' }}>
            {head(['分類', '編號', 'UVa', '題目', '歷屆', '狀態', ''])}
            <tbody>{extra.map((p) => row(p.id, '—', p.title, p.category ?? '其他'))}</tbody>
          </table>
        </>
      )}
    </>
  )
}
