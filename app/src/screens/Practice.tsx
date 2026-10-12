// 練習區（模擬器額外功能，不是考場畫面）：可以自由挑 CPE26 任一題，解題視窗改用碼錶、不計分。

import { useEffect, useState } from 'react'
import { api } from '../judge/api'
import type { ProblemMeta } from '../judge/types'
import { CPE26 } from '../exam/cpe26'
import { useSession } from '../exam/session'
import { Window } from '../winforms/Window'

export function PracticeWindow() {
  const session = useSession()
  const [bank, setBank] = useState<ProblemMeta[]>([])
  useEffect(() => {
    api.problems().then(setBank)
  }, [])

  const inBank = new Set(bank.map((p) => p.id))
  const extra = bank.filter((p) => !CPE26.some((c) => String(c.uva) === p.id))
  const solvedCount = CPE26.filter((c) => session?.practice[String(c.uva)]?.solvedAtMs).length

  const row = (id: string, cpe: string, title: string, category: string) => {
    const rec = session?.practice[id]
    const available = inBank.has(id)
    return (
      <tr key={id}>
        <td>{category}</td>
        <td>{cpe}</td>
        <td>UVA{id}</td>
        <td>{title}</td>
        <td style={{ textAlign: 'center' }}>
          {rec?.solvedAtMs ? <b style={{ color: 'red' }}>通過</b> : rec?.attempts ? `嘗試 ${rec.attempts} 次` : ''}
        </td>
        <td>
          {available ? (
            <a onClick={() => api.openSolveWindow('practice', id, `PRAC.UVA${id}評量:${title}`)}>練習</a>
          ) : (
            <span style={{ color: '#999' }}>尚未收錄</span>
          )}
        </td>
      </tr>
    )
  }

  return (
    <Window title="練習區">
      <div className="ie-page" style={{ padding: '10px 14px' }}>
        <h1 style={{ fontSize: 24 }}>練習區：CPE26 選集</h1>
        <div style={{ fontSize: 14, marginBottom: 8 }}>
          2027 年起，每次 CPE 會有一題選自 CPE26 選集。這裡的解題視窗和考場相同，但計時器改成碼錶、正式評判不計罰時。
          已通過 <b>{solvedCount}</b> / {CPE26.length} 題（收錄 {CPE26.filter((c) => inBank.has(String(c.uva))).length} 題）。
        </div>
        <table className="build-table" style={{ fontSize: 14, width: 'auto' }}>
          <thead>
            <tr>
              {['分類', '編號', 'UVa', '題目', '狀態', ''].map((h) => (
                <th key={h} style={{ border: '1px solid #aaa', background: '#eee', padding: '2px 6px' }}>
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {CPE26.map((c) => row(String(c.uva), `cpe${c.cpe}`, c.title, c.category))}
            {extra.map((p) => row(p.id, '—', p.title, '其他'))}
          </tbody>
        </table>
      </div>
    </Window>
  )
}
