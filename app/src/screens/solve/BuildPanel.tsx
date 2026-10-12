// 解題視窗右側的「建置測試(G)」面板（考場上是嵌入的 HTML，由 template.htm 套版）。
// 版面依圖 1.4.1、1.4.3、1.4.11，見 docs/ui-spec.md §3。

import { useState } from 'react'
import type { Examinee, TestCaseView, Verdict } from '../../judge/types'
import { IdCard } from '../MainWindow'

export type JudgeBadge = '未評判' | '通過' | '未通過暗中測資' | '評判中'

const badgeStyle: Record<JudgeBadge, React.CSSProperties> = {
  未評判: { background: '#98fb98', color: '#000', border: '1px solid #00f' },
  評判中: { background: '#98fb98', color: '#000', border: '1px solid #00f' },
  通過: { background: 'red', color: 'yellow', fontWeight: 'bold', border: '1px solid red' },
  未通過暗中測資: { background: 'black', color: 'yellow', fontWeight: 'bold', border: '1px solid red' },
}

/** 把換行標成 ↵（考場的輸出對照表就是這樣顯示）。 */
function withReturns(s: string | null | undefined): string {
  if (!s) return ''
  return s.replace(/\r?\n/g, '↵\n')
}

/** 逐行比對：相同的行藍字白底、不同的行紅字黃底（template.htm 的 .same / .diff）。 */
function DiffLines({ text, other }: { text: string | null | undefined; other: string | null | undefined }) {
  if (text == null) return null
  const mine = withReturns(text).split('\n')
  const theirs = other == null ? null : withReturns(other).split('\n')
  return (
    <>
      {mine.map((line, i) =>
        line === '' && i === mine.length - 1 ? null : (
          <div key={i} className={theirs === null || theirs[i] === line ? 'same' : 'diff'}>
            {line || '\u00a0'}
          </div>
        ),
      )}
    </>
  )
}

export interface BuildPanelProps {
  examinee: Examinee | null
  badge: JudgeBadge
  words: number
  chars: number
  /** 第幾次測試與結果，例如 2:CORRECT；尚未測試為 null */
  last: { count: number; verdict: Verdict } | null
  problemCode: string
  problemTitle: string
  compileMessage: string | null
  input: string
  onInputChange: (v: string) => void
  shown: TestCaseView | null
  caseSummary: string | null
}

export function BuildPanel(p: BuildPanelProps) {
  const [rows, setRows] = useState(6)
  const [showSyntax, setShowSyntax] = useState(false)
  const [showSemantics, setShowSemantics] = useState(true)
  const [showProblem, setShowProblem] = useState(false)
  const correct = p.last?.verdict === 'CORRECT'

  // 配色照圖 1.4.1：題目資料、語意檢測是淡綠；語法規範、語量規範是藍底黃字
  const green: React.CSSProperties = { background: 'palegreen', border: '1px solid blue', color: '#000' }
  const blue: React.CSSProperties = { background: 'blue', color: 'yellow', border: '1px solid red' }

  return (
    <div className="ie-page" style={{ padding: '4px 6px', fontSize: 15 }}>
      <div style={{ border: '1px solid #aaa', padding: 3, display: 'inline-block' }}>
        {p.examinee ? (
          <IdCard idNo={p.examinee.idNo} name={p.examinee.name} ticket={p.examinee.ticket} authCode={p.examinee.authCode} size={20} />
        ) : (
          <IdCard idNo="練習區" name="模擬考生" ticket="—" authCode="—" size={20} />
        )}
      </div>

      <div style={{ marginTop: 22, display: 'flex', alignItems: 'center', gap: 4 }}>
        <span style={{ border: '1px solid #00f', padding: 1 }}>
          <span style={{ display: 'inline-block', minWidth: 104, textAlign: 'center', padding: '2px 10px', whiteSpace: 'nowrap', ...badgeStyle[p.badge] }}>{p.badge}</span>
        </span>
        <span>
          {p.words}詞，{p.chars}字元。
        </span>
      </div>

      <div style={{ marginTop: 22, minHeight: 24 }}>
        {p.last && (
          <span
            style={{
              display: 'inline-block',
              padding: '0 2px',
              border: '3px double',
              borderColor: correct ? 'blue' : 'red',
              color: correct ? 'blue' : 'red',
              fontWeight: 'bold',
            }}
          >
            {p.last.count}:{p.last.verdict}
          </span>
        )}
      </div>

      <div style={{ marginTop: 14 }}>
        <button className="ie-tab-btn" style={green} onClick={() => setShowProblem(!showProblem)}>
          題目資料
        </button>{' '}
        <span style={{ border: '1px solid red', fontWeight: 'bold' }}>
          ({p.problemCode}) {p.problemTitle} :
        </span>
      </div>
      <div style={{ marginTop: 2 }}>
        <button className="ie-tab-btn" style={blue} onClick={() => setShowSyntax(!showSyntax)}>
          語法規範
        </button>{' '}
        <button className="ie-tab-btn" style={blue}>
          語量規範(0)
        </button>
      </div>
      {showSyntax && (
        <div style={{ margin: '4px 0', fontSize: 12 }}>
          <small>您編譯資訊是由向外呼叫編(直)譯器所產生，編(直)譯器廠商商標歸屬於其合法擁有者，特此聲明。</small>
          <pre style={{ margin: '4px 0', whiteSpace: 'pre-wrap', fontSize: 12, color: p.compileMessage ? '#c00' : '#000' }}>
            {p.compileMessage ?? '（編譯成功，沒有訊息）'}
          </pre>
        </div>
      )}

      <div style={{ marginTop: 14 }}>
        <button className="ie-tab-btn" style={green} onClick={() => setShowSemantics(!showSemantics)}>
          語意檢測
        </button>{' '}
        <button className="wf-button" style={{ minWidth: 0 }} onClick={() => setRows(rows + 5)}>
          輸入區放大
        </button>{' '}
        <button className="wf-button" style={{ minWidth: 0 }} onClick={() => setRows(Math.max(1, rows - 5))}>
          輸入區縮小
        </button>
      </div>

      {showSemantics && (
        <>
          <table className="build-table" style={{ marginTop: 4 }}>
            <tbody>
              <tr>
                <td style={{ width: 92 }}>標準輸入串</td>
                <td>
                  <textarea
                    rows={rows}
                    value={p.input}
                    onChange={(e) => p.onInputChange(e.target.value)}
                    spellCheck={false}
                    style={{ width: '100%', fontFamily: 'var(--code-font)', fontSize: 12, resize: 'vertical' }}
                  />
                </td>
              </tr>
            </tbody>
          </table>
          {p.caseSummary && <div style={{ fontSize: 12, color: '#555', margin: '2px 0' }}>{p.caseSummary}</div>}
          <table className="build-table">
            <tbody>
              <tr>
                <td style={{ width: 46 }}>您的輸出串</td>
                <td className="out">
                  <DiffLines text={p.shown?.stdout} other={p.shown?.expected} />
                </td>
                <td style={{ width: 46 }}>正確輸出串</td>
                <td className="out">
                  <DiffLines text={p.shown?.expected} other={p.shown?.stdout} />
                </td>
              </tr>
              <tr>
                <td>您的錯誤串</td>
                <td className="out">{p.shown?.stderr}</td>
                <td>正確錯誤串</td>
                <td className="out" />
              </tr>
              <tr>
                <td>您的耗時(GCS)</td>
                <td className="out">{p.shown ? (p.shown.timeMs / 1000).toFixed(6) : ''}</td>
                <td>標準耗時(GCS)</td>
                <td className="out">{p.shown?.expectedTimeMs != null ? (p.shown.expectedTimeMs / 1000).toFixed(6) : ''}</td>
              </tr>
            </tbody>
          </table>
        </>
      )}
    </div>
  )
}
