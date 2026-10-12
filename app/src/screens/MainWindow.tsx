// 主畫面：上方 WinForms 工具列 + 嵌入的 IE 網頁（授權 → 登入 → 題目列表）。
// 版面依考生使用手冊圖 1.1.1、1.1.2、1.1.3、1.2.1，見 docs/ui-spec.md §1、§2。

import { useEffect, useState } from 'react'
import { api } from '../judge/api'
import type { ProblemMeta, Session, ToolchainReport } from '../judge/types'
import { drawExam, percentileFor, scoreExam } from '../exam/scoring'
import {
  formatMonthDayHm,
  formatMonthDayHms,
  formatRemainingShort,
  isExamOver,
  problemCode,
  remainingMs,
  useNow,
  useSession,
} from '../exam/session'
import { Window } from '../winforms/Window'
import { MenuBar, type MenuEntry } from '../winforms/MenuBar'
import { useDialogs } from '../winforms/Dialogs'

const APP_TITLE = '大學程式能力檢定'

export function MainWindow() {
  const session = useSession()
  const [bank, setBank] = useState<ProblemMeta[]>([])
  useEffect(() => {
    api.problems().then(setBank)
  }, [])

  if (!session) return <Window title={APP_TITLE}>{null}</Window>
  return (
    <Window title={APP_TITLE}>
      <Toolbar session={session} />
      <div className="ie-page">
        {session.phase === 'license' && <LicensePage />}
        {session.phase === 'login' && <LoginPage bank={bank} />}
        {session.phase === 'exam' && <ExamPage session={session} bank={bank} />}
      </div>
    </Window>
  )
}

// ───────────── 上方工具列 ─────────────

function Toolbar({ session }: { session: Session }) {
  const now = useNow()
  const dialogs = useDialogs()
  const exam = session.exam
  const remaining = exam ? remainingMs(exam, now) : 0
  const loggedIn = session.phase === 'exam'

  const notInSim = () => dialogs.message('瘋狂程設', '模擬考場不提供此功能。', { icon: 'info' })

  const studentMenu: MenuEntry[] = [
    { label: '考生手冊', mnemonic: 'H', after: '(Handouts)', onSelect: () => dialogs.message('考生手冊(Handouts)', '請參考 CPE 官網「環境與教材」的考生使用手冊。', { icon: 'info' }) },
    { label: '電子發問', mnemonic: 'Q', after: '(Clarification Request)', onSelect: notInSim },
    { label: '問題回應', mnemonic: 'A', after: '(Clarification Response)', onSelect: notInSim },
    { label: '考生問卷', mnemonic: 'T', after: '(Questionaire)', onSelect: notInSim },
    { sep: true },
    { label: '練習成績', mnemonic: 'P', after: '(Score Board (Practice))', onSelect: () => api.openToolWindow('scoreboard', '練習成績') },
    { label: '聯賽成績', mnemonic: 'G', after: '(Score Board)', onSelect: () => api.openToolWindow('scoreboard', '聯賽成績') },
    { label: '教室成績', mnemonic: 'M', after: '(Score Board)', onSelect: () => api.openToolWindow('scoreboard', '教室成績') },
    { sep: true },
    { label: 'Java參考資料', mnemonic: 'J', after: '(Java Reference)', disabled: true },
    { label: 'C++參考資料', mnemonic: 'C', after: '(C++ Reference)', disabled: true },
    { label: '英漢字典', mnemonic: 'E', after: '(Dictionary)', onSelect: () => api.openToolWindow('dictionary', '英漢字典') },
    { sep: true },
    { label: '維修：更新主頁', mnemonic: 'R', onSelect: () => location.reload() },
    { label: '維修：取得考試題目', onSelect: () => location.reload() },
    { label: '維修：緊急維修', mnemonic: 'P', onSelect: notInSim },
    { sep: true },
    { label: '【模擬器】練習區', mnemonic: 'Z', onSelect: () => api.openToolWindow('practice', '練習區') },
  ]

  const examinerManage = async () => {
    const pw = await dialogs.prompt('考官管理', '請輸入考官密碼（模擬考場：任意輸入即可）')
    if (pw === null) return
    const choice = await dialogs.message('考官管理', '請選擇要執行的動作。', {
      icon: 'question',
      buttons: ['重新開始模擬考', '取消'],
      defaultIndex: 1,
    })
    if (choice === 0) await api.sessionReset()
  }

  const endExam = async () => {
    if (!exam || isExamOver(exam, now)) return
    if (await dialogs.confirm('結束評量', '結束本次考試後將無法再送繳程式，您確定要結束評量嗎?')) await api.sessionEndExam()
  }

  return (
    <div className="main-toolbar">
      <div className="menu-red" style={{ display: 'flex' }}>
        <MenuBar menus={[{ label: '考生功能', mnemonic: 'S', items: studentMenu }]} />
      </div>
      {exam && (
        <span>
          {formatMonthDayHm(exam.startedAtMs)} ~ {formatMonthDayHm(exam.startedAtMs + exam.durationMs)}
        </span>
      )}
      <span className="examiner" onClick={examinerManage}>
        考官管理(T)
      </span>
      <span>{formatMonthDayHms(now)}</span>
      <span className="host">我是考生機：模擬考場（本機評判）</span>
      <span style={{ flex: 1 }} />
      {loggedIn && exam && (
        <>
          <div className="wf-progress" style={{ width: 100 }}>
            <div style={{ width: `${(remaining / exam.durationMs) * 100}%` }} />
          </div>
          <span className="apple">🍎</span>
          <span>{formatRemainingShort(remaining)}</span>
        </>
      )}
      <button className="end-exam" onClick={endExam}>
        結束評量
      </button>
    </div>
  )
}

// ───────────── 授權頁（圖 1.1.1） ─────────────

function LicensePage() {
  const [tools, setTools] = useState<ToolchainReport | null>(null)
  const [installing, setInstalling] = useState(false)

  useEffect(() => {
    api.toolchainStatus().then(setTools)
  }, [])
  useEffect(() => {
    if (!installing) return
    const t = setInterval(async () => {
      const r = await api.toolchainStatus()
      setTools(r)
      if (r.commandLineToolsInstalled) setInstalling(false)
    }, 3000)
    return () => clearInterval(t)
  }, [installing])

  const links = ['本軟體授權', 'Alsing.SyntaxBox', 'WinFormsUI', 'HybridDSP', 'DotNetFireball', 'Watcom C++', 'PHP', 'Json.Net']
  const missing = tools?.tools.filter((t) => !t.program) ?? []

  return (
    <div style={{ display: 'flex', minHeight: '100%' }}>
      <div style={{ width: 160, flex: 'none', background: '#e6e6e6', padding: '14px 10px', fontFamily: 'var(--wf-font)' }}>
        <button className="wf-button" style={{ width: '100%', height: 30, outline: '2px solid #e00' }} onClick={() => api.sessionAgreeLicense()}>
          同意以下各授權規定
        </button>
        <div style={{ margin: '22px 6px', lineHeight: '22px', fontFamily: 'var(--html-font)', fontSize: 12 }}>
          {links.map((l) => (
            <div key={l}>
              <span className="ie-link">{l}</span>
            </div>
          ))}
        </div>
        <button className="wf-button" style={{ width: '100%', height: 30, marginTop: 70 }} disabled>
          返回考場
        </button>
      </div>
      <div style={{ padding: '10px 18px', flex: 1 }}>
        {tools && (!tools.commandLineToolsInstalled || missing.length > 0) && (
          <div className="sim-box" style={{ margin: '0 0 12px', borderColor: '#d39b00', background: '#fff8e0' }}>
            <b>【模擬器】</b>
            {!tools.commandLineToolsInstalled ? (
              <>
                這台 Mac 尚未安裝 Xcode Command Line Tools（提供 C/C++ 編譯器與 Python）。{' '}
                <button className="wf-button" disabled={installing} onClick={() => api.installCommandLineTools().then(() => setInstalling(true))}>
                  {installing ? '安裝中…請依系統視窗指示完成' : '安裝'}
                </button>
              </>
            ) : (
              <>找不到下列編譯器：{missing.map((m) => m.display).join('、')}</>
            )}
          </div>
        )}
        <h1 style={{ fontWeight: 'bold', textDecoration: 'underline', fontSize: 30 }}>大學程式能力檢定</h1>
        <br />
        <br />
        <LicenseSection title="使用方法">
          <ol>
            <li>本軟體需搭配編(直)譯器使用，請根據支援選擇適當的或內建的編(直)譯器。</li>
            <li>編譯器使用需自行取得選擇編譯器或直譯器的授權，且取得之授權需無礙於搭配本軟體使用。</li>
            <li>
              本模擬考場支援的編譯器如下：
              <ol>
                <li>CCPP：本機的 g++ / clang++（Mac 由 Xcode Command Line Tools 提供）。</li>
                <li>PYTH：本機的 Python 3。</li>
              </ol>
            </li>
          </ol>
        </LicenseSection>
        <LicenseSection title="軟體引用">
          <ul>
            <li>本模擬考場為非官方軟體，與 CPE 委員會、瘋狂程設作者無關。</li>
            <li>題目敘述為自行改寫，原題版權屬 UVa Online Judge。</li>
            <li>本軟體使用第三方函式庫，相關授權請見各函式庫之授權聲明。</li>
          </ul>
        </LicenseSection>
      </div>
    </div>
  )
}

function LicenseSection({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div style={{ marginBottom: 18 }}>
      <span style={{ display: 'inline-block', padding: '2px 4px', background: '#ccc', border: '2px solid #000', fontWeight: 'bold', fontSize: 20 }}>
        {title}
      </span>
      <div style={{ fontSize: 15 }}>{children}</div>
    </div>
  )
}

// ───────────── 登入頁（圖 1.1.2） ─────────────

function Notices() {
  return (
    <>
      <div style={{ marginTop: 6 }}>
        <span className="ie-alttab">ALT + TAB</span> 可以切換不同視窗。
      </div>
      <ul>
        <li className="ie-red">監考機址：模擬考場（本機評判）</li>
        <li>
          如果此處題目區未能於適當時間顯示題目資訊，請按 <span className="ie-hilite">F5</span> 更新。
        </li>
        <li>Java 程式撰寫 請使用 class main，按 ALT+L 選 Java編譯器，CTRL+H 可以觀察雙和範例。</li>
        <li>Java 程式撰寫 換行 請使用 "\r\n" 不要只使用 "\n"。</li>
        <li className="ie-red">程式通過繳交，請務必按 [桌面/考生功能/考場成績](這是及時資料)，確認資料是否上傳監考機，確認資料是否有誤。</li>
      </ul>
    </>
  )
}

function LoginPage({ bank }: { bank: ProblemMeta[] }) {
  const dialogs = useDialogs()
  const [idNo, setIdNo] = useState('')
  const [ticket, setTicket] = useState('')

  const login = async () => {
    if (!idNo.trim() || !ticket.trim()) {
      await dialogs.message('登入', '請填寫身分證字號與准考碼。', { icon: 'info' })
      return
    }
    const picked = drawExam(bank)
    try {
      await api.sessionLogin(idNo, ticket, picked.map((p) => p.id))
    } catch (e) {
      await dialogs.message('登入', String(e), { icon: 'info' })
    }
  }

  return (
    <div style={{ padding: '30px 8px 0' }}>
      <div style={{ borderTop: '1px solid #000', borderBottom: '1px solid #000', padding: '6px 0', width: 'max-content', minWidth: 700 }}>
        <form
          onSubmit={(e) => {
            e.preventDefault()
            login()
          }}
          style={{ outline: '3px solid #e00', padding: 4, width: 580, fontSize: 15 }}
        >
          <div style={{ color: 'red' }}>
            (請詳細檢查，切勿填錯，填錯需重領<span style={{ color: 'blue' }}>准考單</span>應考。)
          </div>
          <table>
            <tbody>
              <tr>
                <td>(A)身分證字號或護照號碼</td>
                <td>
                  <input className="wf-textbox" style={{ width: 155 }} value={idNo} onChange={(e) => setIdNo(e.target.value)} autoFocus />
                </td>
              </tr>
              <tr>
                <td>(C)准考碼</td>
                <td>
                  <input className="wf-textbox" style={{ width: 155 }} value={ticket} onChange={(e) => setTicket(e.target.value)} />{' '}
                  <button type="submit" className="wf-button" style={{ minWidth: 0 }}>
                    確認登入
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </form>
      </div>
      <Notices />
      <h1>題目</h1>
      <span style={{ display: 'inline-block', border: '3px double #000', padding: '1px 3px', fontSize: 15 }}>請先登入系統</span>
      <h1 style={{ marginTop: 22 }}>大學程式能力檢定(CPE)考生注意事項</h1>
      <ol style={{ fontSize: 15 }}>
        <li>
          考試時程（模擬考場：登入後立即開始，共 3 小時）：
          <ol>
            <li>考生報到時間：17:30~17:40。</li>
            <li>考生進行考試環境測試：17:40~18:30。</li>
            <li>休息與準備：18:30~18:40。</li>
            <li>正式考試：18:40~21:40。</li>
            <li className="ie-red">考生於 18:00 後，不准入場。</li>
            <li>考生於 19:40 後，後，始得離場不再考試。</li>
          </ol>
        </li>
      </ol>
      <div className="sim-box">
        <b>【模擬器】</b>身分證字號與准考碼可任意填寫。登入後會從題庫抽出 7 題（較簡單的三題排在前三題），立即開始 3 小時的模擬考。
        想先自由練習可以使用 <span className="ie-link" onClick={() => api.openToolWindow('practice', '練習區')}>練習區</span>。
      </div>
    </div>
  )
}

// ───────────── 登入後：題目列表（圖 1.1.3） ─────────────

function ExamPage({ session, bank }: { session: Session; bank: ProblemMeta[] }) {
  const now = useNow()
  const exam = session.exam!
  const e = session.examinee!
  const over = isExamOver(exam, now)
  const meta = (id: string) => bank.find((p) => p.id === id)

  const open = (mode: 'exam' | 'view', id: string, label: string) => {
    const m = meta(id)
    const code = problemCode(label, m?.uva ?? null, id)
    api.openSolveWindow(mode, id, mode === 'view' ? `${code} ${m?.title ?? ''}` : `${code}評量:${m?.title ?? ''}`)
  }

  return (
    <div style={{ padding: '30px 8px 20px' }}>
      <IdCard idNo={e.idNo} name={e.name} ticket={e.ticket} authCode={e.authCode} />
      <Notices />
      <h1>題目</h1>
      <div className="ie-problems">
        <table>
          <tbody>
            <tr>
              <td colSpan={3} style={{ border: 'none' }}>
                請慢慢開題!! (點擊之後 請等待!!)
                <div className="ie-red" style={{ fontSize: 17 }}>
                  正式考題 {exam.code}
                </div>
              </td>
            </tr>
            {exam.problems.map((p) => (
              <tr key={p.problemId}>
                <td>
                  <a onClick={() => open('exam', p.problemId, p.label)}>解題</a>
                </td>
                <td>{problemCode(p.label, meta(p.problemId)?.uva ?? null, p.problemId)}</td>
                <td>
                  <a onClick={() => open('view', p.problemId, p.label)}>看題</a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {over && <ResultBox session={session} />}
    </div>
  )
}

export function IdCard({ idNo, name, ticket, authCode, size = 24 }: { idNo: string; name: string; ticket: string; authCode: string; size?: number }) {
  return (
    <div>
      <table className="ie-idcard" style={{ fontSize: size }}>
        <tbody>
          <tr>
            <td style={{ fontSize: size }}>(A) {idNo}</td>
            <td style={{ fontSize: size }}>(B) {name}</td>
          </tr>
          <tr>
            <td style={{ fontSize: size }}>(C) {ticket}</td>
            <td style={{ fontSize: size }}>(D) {authCode}</td>
          </tr>
        </tbody>
      </table>
      <div style={{ fontSize: 15 }}>(A:身分證,B:姓名字,C:准考碼,D:認證碼)</div>
    </div>
  )
}

/** 模擬器加的成績報告（考場沒有，考後才看得到成績）。 */
function ResultBox({ session }: { session: Session }) {
  const exam = session.exam!
  const score = scoreExam(
    exam.problems.map((p) => p.problemId),
    exam.submissions,
  )
  return (
    <div className="sim-box" style={{ fontSize: 15 }}>
      <b>【模擬器】本次模擬考已結束</b>
      <div style={{ marginTop: 6 }}>
        答對 <b style={{ color: '#c00', fontSize: 20 }}>{score.solved}</b> 題，總耗時 {score.totalTime} 分（含罰時）。
        對照官方 2022/3 場次的成績分布，約贏過 <b>{percentileFor(score.solved)}%</b> 的考生。
      </div>
      <div style={{ marginTop: 8 }}>
        <button className="wf-button" onClick={() => api.openToolWindow('scoreboard', '聯賽成績')}>
          查看成績表
        </button>{' '}
        <button className="wf-button" onClick={() => api.sessionReset()}>
          重新開始模擬考
        </button>
      </div>
    </div>
  )
}
