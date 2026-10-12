// 歷屆考古題（模擬器額外功能）：依日期列出 CPE 官方「歷次考題一覽」的每一場。
// 每題標示官方考生答對率與題型；題目都已收錄的場次可以「整場重考」。

import { useState } from 'react'
import { api } from '../judge/api'
import type { ProblemMeta, Session } from '../judge/types'
import { HISTORY, displayTitle, formatDate, tagsOf } from '../exam/history'
import { useDialogs } from '../winforms/Dialogs'

const TEN_YEARS_FROM = '2016-01-01'

export function HistoryTab({ bank, session }: { bank: ProblemMeta[]; session: Session | null }) {
  const dialogs = useDialogs()
  const [all, setAll] = useState(false)
  const [onlyPlayable, setOnlyPlayable] = useState(false)
  const inBank = new Set(bank.map((p) => p.id))

  const exams = [...HISTORY]
    .reverse()
    .filter((e) => all || e.date >= TEN_YEARS_FROM)
    .filter((e) => !onlyPlayable || e.problems.every((p) => inBank.has(String(p.uva))))

  const replay = async (date: string, ids: string[]) => {
    const title = `${formatDate(date)} CPE 考古題`
    const ok = await dialogs.confirm('整場重考', `要用「${title}」的 ${ids.length} 題開始一場 3 小時的模擬考嗎？\n目前進行中的模擬考會被清除。`)
    if (!ok) return
    await api.sessionPlanExam(title, ids)
    await dialogs.message('整場重考', '已設定考卷，請到主畫面輸入身分證字號與准考碼登入，登入後立即開考。', { icon: 'info' })
  }

  const open = (uva: number, title: string) => api.openSolveWindow('practice', String(uva), `PRAC.UVA${uva}評量:${title}`)

  return (
    <div>
      <div style={{ fontSize: 14, margin: '4px 0 10px' }}>
        資料來源：CPE 官方「歷次考題一覽」，共 {HISTORY.length} 場（{formatDate(HISTORY[0].date)} ~ {formatDate(HISTORY[HISTORY.length - 1].date)}）。
        「考生答對率」是答對人數除以全體考生人數。
        <div style={{ marginTop: 4, fontFamily: 'var(--wf-font)', fontSize: 12 }}>
          <label>
            <input type="checkbox" checked={all} onChange={(e) => setAll(e.target.checked)} /> 顯示 2016 年以前的考試
          </label>{' '}
          <label style={{ marginLeft: 12 }}>
            <input type="checkbox" checked={onlyPlayable} onChange={(e) => setOnlyPlayable(e.target.checked)} /> 只顯示可以整場重考的場次
          </label>
        </div>
      </div>
      {exams.length === 0 && <div style={{ color: '#777' }}>沒有符合條件的場次。</div>}
      {exams.map((e) => {
        const ids = e.problems.map((p) => String(p.uva))
        const have = ids.filter((id) => inBank.has(id)).length
        return (
          <div key={e.date} style={{ marginBottom: 16 }}>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: 12, borderBottom: '2px solid #0070e8', marginBottom: 4 }}>
              <b style={{ fontSize: 18, color: '#0070e8' }}>{formatDate(e.date)} CPE</b>
              <span style={{ fontSize: 13 }}>平均答對 {e.avgSolved} 題</span>
              <span style={{ fontSize: 13, color: have === ids.length ? '#080' : '#777' }}>
                已收錄 {have}/{ids.length}
              </span>
              {have === ids.length && (
                <button className="wf-button" style={{ minWidth: 0, marginLeft: 'auto', marginBottom: 2 }} onClick={() => replay(e.date, ids)}>
                  整場重考
                </button>
              )}
            </div>
            <table className="build-table" style={{ fontSize: 13 }}>
              <tbody>
                {e.problems.map((p) => {
                  const id = String(p.uva)
                  const rec = session?.practice[id]
                  return (
                    <tr key={p.pos}>
                      <td style={{ width: 28, textAlign: 'center' }}>P{p.pos}</td>
                      <td style={{ width: 72 }}>UVA{p.uva}</td>
                      <td>
                        {displayTitle(p)}
                        {p.uvaTitle && (
                          <span title={`官方清單題名為「${p.title}」，與 UVa ${p.uva} 不符；本模擬器以編號為準`} style={{ color: '#c60', cursor: 'help' }}>
                            {' '}
                            ⚠
                          </span>
                        )}
                      </td>
                      <td style={{ width: 150, color: '#555' }}>{tagsOf(p.uva).join('、')}</td>
                      <td style={{ width: 120 }}>
                        <RateBar value={p.rateAll} />
                      </td>
                      <td style={{ width: 70, textAlign: 'center' }}>
                        {rec?.solvedAtMs ? <b style={{ color: 'red' }}>通過</b> : null}
                        {!rec?.solvedAtMs && (inBank.has(id) ? <a onClick={() => open(p.uva, displayTitle(p))}>練習</a> : <span style={{ color: '#aaa' }}>尚未收錄</span>)}
                      </td>
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>
        )
      })}
    </div>
  )
}

/** 考生答對率：數字加上一條橫條，一眼看出難易。 */
function RateBar({ value }: { value: number }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
      <div style={{ width: 50, height: 8, background: '#e8e8e8' }}>
        <div style={{ width: `${Math.min(100, value)}%`, height: '100%', background: '#3d8bd9' }} />
      </div>
      <span style={{ fontVariantNumeric: 'tabular-nums' }}>{value.toFixed(1)}%</span>
    </div>
  )
}
