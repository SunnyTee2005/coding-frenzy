// 解題視窗：每題一個獨立視窗。
// 選單、Dock 版面、對話框依考生使用手冊圖 1.4.1 ~ 1.4.13，見 docs/ui-spec.md §3。
// mode = 'exam'（倒數計時、送繳列入成績）、'practice'（碼錶、不計分）、'view'（看題：只顯示題文）。

import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { api } from '../judge/api'
import type { Language, Mode, ProblemDetail, TestCaseView, TestRun, ToolchainReport, Verdict } from '../judge/types'
import { formatHms, isExamOver, problemCode, remainingMs, useNow, useSession } from '../exam/session'
import { Window } from '../winforms/Window'
import { MenuBar, type MenuEntry } from '../winforms/MenuBar'
import { useDialogs } from '../winforms/Dialogs'
import { DockPane, Splitter } from '../winforms/Dock'
import { CodeEditor } from '../editor/CodeEditor'
import { BuildPanel, type JudgeBadge } from './solve/BuildPanel'

export function SolveWindow({ mode, problemId }: { mode: Mode | 'view'; problemId: string }) {
  const [problem, setProblem] = useState<ProblemDetail | null>(null)
  useEffect(() => {
    api.problem(problemId).then(setProblem)
  }, [problemId])
  if (!problem) return <Window title="">{null}</Window>
  if (mode === 'view') return <StatementOnly problem={problem} />
  return <Solver mode={mode} problem={problem} />
}

function Statement({ html }: { html: string }) {
  return <div className="uva-statement" dangerouslySetInnerHTML={{ __html: html }} />
}

/** 「看題」：只看題文，不開編輯器。 */
function StatementOnly({ problem }: { problem: ProblemDetail }) {
  return (
    <Window title={`UVA${problem.meta.uva ?? problem.meta.id} ${problem.meta.title}`}>
      <div className="ie-page">
        <Statement html={problem.statement} />
      </div>
    </Window>
  )
}

// 考場編譯器選單（圖 1.4.10）。只有 CCPP:MinGW 與 Python 在模擬考場可用，其餘照考場顯示為灰色。
const FAKE_COMPILERS: (string | null)[] = [
  'MSVC:Microsoft Visual Studio 10.0',
  null,
  'CCPP:WatCom',
  'CCPP:C',
  null,
  'JAVA:jdk1.7.0_25',
  null,
  'MSCS:v2.0.50727',
  'MSCS:v3.5',
  'MSCS:v4.0.30319',
  null,
  'MSVB:v2.0.50727',
  'MSVB:v3.5',
  'MSVB:v4.0.30319',
  null,
  'MSJS:v2.0.50727',
  'MSJS:v4.0.30319',
]
const COMPILER_MNEMONIC: Record<string, string> = { ccpp: 'M', python: 'P' }

const SAMPLE_CODE: Record<string, string> = {
  ccpp: `//== 以上為雙和範例
/*
#include <iostream>
using namespace std;

int main(){
    int a, b;
    while (cin >> a >> b)
        cout << a + b << endl;
    return 0;
}
*/
`,
  python: `#== 以上為雙和範例
# import sys
# for line in sys.stdin:
#     a, b = map(int, line.split())
#     print(a + b)
`,
}

const DEFAULT_FONT = 16

const pad2 = (n: number) => String(n).padStart(2, '0')
const randHex = (n: number) => Array.from({ length: n }, () => Math.floor(Math.random() * 16).toString(16)).join('')

function Solver({ mode, problem }: { mode: Mode; problem: ProblemDetail }) {
  const dialogs = useDialogs()
  const session = useSession()
  const now = useNow()
  const id = problem.meta.id

  const [langs, setLangs] = useState<Language[]>([])
  const [tools, setTools] = useState<ToolchainReport | null>(null)
  const [lang, setLang] = useState('ccpp')
  const [source, setSource] = useState('')
  const [loaded, setLoaded] = useState(false)
  const [fontSize, setFontSize] = useState(DEFAULT_FONT)

  const [busy, setBusy] = useState(false)
  const [testCount, setTestCount] = useState(0)
  const [last, setLast] = useState<{ count: number; verdict: Verdict } | null>(null)
  const [compileMessage, setCompileMessage] = useState<string | null>(null)
  const [input, setInput] = useState('')
  const [shown, setShown] = useState<TestCaseView | null>(null)
  const [caseSummary, setCaseSummary] = useState<string | null>(null)

  // 版面
  const [show, setShow] = useState({ statement: true, result: true, output: true })
  const [outputTab, setOutputTab] = useState<'mine' | 'expected'>('mine')
  const [statementH, setStatementH] = useState(190)
  const [outputH, setOutputH] = useState(150)
  const [rightW, setRightW] = useState(330)

  // 練習區碼錶
  const [swStart, setSwStart] = useState(() => Date.now())
  const [swPausedAt, setSwPausedAt] = useState<number | null>(null)

  const exam = session?.exam ?? null
  const label = exam?.problems.find((p) => p.problemId === id)?.label ?? 'PRAC'
  const code = problemCode(mode === 'exam' ? label : 'PRAC', problem.meta.uva, id)
  const over = mode === 'exam' && (!exam || isExamOver(exam, now))

  useEffect(() => {
    api.languages().then(setLangs)
    api.toolchainStatus().then(setTools)
    api.draftLoad(mode, id).then((d) => {
      if (d) {
        setLang(d.lang)
        setSource(d.source)
      }
      setLoaded(true)
    })
  }, [mode, id])

  // 自動存草稿（關掉視窗或當機也不會遺失）
  useEffect(() => {
    if (!loaded) return
    const t = setTimeout(() => api.draftSave(mode, { problemId: id, lang, source }), 400)
    return () => clearTimeout(t)
  }, [loaded, mode, id, lang, source])

  const badge: JudgeBadge = useMemo(() => {
    if (busy) return '評判中'
    if (mode === 'exam') {
      const subs = exam?.submissions.filter((s) => s.problemId === id) ?? []
      if (subs.some((s) => s.verdict === 'CORRECT')) return '通過'
      return subs.length ? '未通過暗中測資' : '未評判'
    }
    const rec = session?.practice[id]
    if (rec?.solvedAtMs) return '通過'
    return rec?.attempts ? '未通過暗中測資' : '未評判'
  }, [busy, mode, exam, session, id])

  const available = (langId: string) => !!tools?.tools.find((t) => t.lang_id === langId)?.program

  const record = useCallback(
    (verdict: Verdict) => {
      const count = testCount + 1
      setTestCount(count)
      setLast({ count, verdict })
    },
    [testCount],
  )

  /** 顯示一次測試的結果：有錯的那筆優先，否則顯示最後一筆。 */
  const showRun = (run: TestRun) => {
    setCompileMessage(run.compileMessage)
    record(run.verdict)
    if (run.verdict === 'COMPILER-ERROR') {
      setShown(null)
      setCaseSummary('COMPILER-ERROR：請按「語法規範」查看編譯訊息。')
      return
    }
    const bad = run.cases.find((c) => c.verdict !== 'CORRECT')
    const pick = bad ?? run.cases[run.cases.length - 1] ?? null
    setShown(pick)
    if (pick) setInput(pick.input)
    if (run.cases.length > 1) {
      const passed = run.cases.filter((c) => c.verdict === 'CORRECT').length
      setCaseSummary(`共 ${run.cases.length} 組，通過 ${passed} 組${bad ? `；顯示第一組未通過的測資（${bad.name}）` : ''}`)
    } else setCaseSummary(null)
  }

  const runTests = async (kind: 'sample' | 'public' | 'custom') => {
    if (busy) return
    setBusy(true)
    setLast((l) => (l ? { ...l, verdict: 'PENDING' } : { count: testCount + 1, verdict: 'PENDING' }))
    try {
      const run = kind === 'custom' ? await api.runCustom(id, lang, source, input) : await api.runTests(id, lang, source, kind)
      showRun(run)
    } catch (e) {
      await dialogs.message('瘋狂程設', String(e), { icon: 'info' })
    } finally {
      setBusy(false)
    }
  }

  const formalJudge = async () => {
    if (busy) return
    if (over) {
      await dialogs.message('批改確認', '考試時間已結束，無法再批改。', { icon: 'info' })
      return
    }
    if (badge === '通過') {
      await dialogs.message('批改確認', '本題已經通過，不需要再批改。', { icon: 'info' })
      return
    }
    const ok = await dialogs.confirm('批改確認', mode === 'exam' ? '批改錯誤將罰扣20分鐘，您確定要批改嗎?' : '練習區不計罰時，您確定要批改嗎?')
    if (!ok) return
    setBusy(true)
    try {
      const r = await api.formalJudge(mode, id, lang, source)
      setCompileMessage(r.compileMessage)
      record(r.verdict)
    } catch (e) {
      await dialogs.message('批改確認', String(e), { icon: 'info' })
    } finally {
      setBusy(false)
    }
  }

  const timeTag = () => {
    const d = new Date()
    return [d.getHours(), d.getMinutes(), d.getSeconds()].map(pad2)
  }

  const sealSave = async () => {
    const [h, m, s] = timeTag()
    await api.saveCode(`(${h}-${m}-${s})${randHex(8)}-${randHex(4)}-${randHex(4)}@${randHex(32)}@main.cpp`, { problemId: id, lang, source })
  }

  const saveAs = async () => {
    const name = await dialogs.prompt('', '請輸入檔名')
    if (!name) return
    const [h, m, s] = timeTag()
    await api.saveCode(`${name}-(${h};${m};${s})-${randHex(8)}@${randHex(32)}@main.cpp`, { problemId: id, lang, source })
  }

  const resume = async () => {
    const saves = await api.savesList()
    const idx = await dialogs.pickFromList('', saves.map((s) => s.name))
    if (idx === null) return
    setLang(saves[idx].lang)
    setSource(saves[idx].source)
  }

  const pasteSample = () => setSource((s) => (s.endsWith('\n') || s === '' ? s : s + '\n') + (SAMPLE_CODE[lang] ?? SAMPLE_CODE.ccpp))

  const words = source.split(/\s+/).filter(Boolean).length
  const currentLang = langs.find((l) => l.id === lang)

  // ───────── 選單 ─────────
  const compilerItems: MenuEntry[] = [
    ...FAKE_COMPILERS.slice(0, 2).map((c): MenuEntry => (c ? { label: `${c}(0)`, disabled: true, icon: '⊘' } : { sep: true })),
    ...langs
      .filter((l) => l.id === 'ccpp')
      .map((l): MenuEntry => ({ label: l.display, mnemonic: COMPILER_MNEMONIC[l.id], checked: l.id === lang, disabled: !available(l.id), onSelect: () => setLang(l.id) })),
    ...FAKE_COMPILERS.slice(2, 5).map((c): MenuEntry => (c ? { label: c, disabled: true, icon: '⊘' } : { sep: true })),
    { label: 'JAVA:jdk1.7.0_25(7)', disabled: true, icon: '⊘' },
    { sep: true },
    ...langs
      .filter((l) => l.id === 'python')
      .map((l): MenuEntry => ({ label: l.display, mnemonic: COMPILER_MNEMONIC[l.id], checked: l.id === lang, disabled: !available(l.id), onSelect: () => setLang(l.id) })),
    ...FAKE_COMPILERS.slice(6).map((c): MenuEntry => (c ? { label: c, disabled: true, icon: '⊘' } : { sep: true })),
  ]

  const toggle = (k: keyof typeof show, v?: boolean) => setShow((s) => ({ ...s, [k]: v ?? !s[k] }))

  const menus = [
    { label: '正式評判', mnemonic: 'J', bold: true, boxed: true, onSelect: formalJudge },
    {
      label: '檔案',
      mnemonic: 'F',
      items: [
        { label: '提檔續答', mnemonic: 'W', shortcut: 'Ctrl+W', onSelect: resume },
        { label: '封卷存檔', mnemonic: 'S', shortcut: 'Ctrl+S', onSelect: sealSave },
        { label: '另存新檔', mnemonic: 'A', shortcut: 'Ctrl+N', onSelect: saveAs },
      ] as MenuEntry[],
    },
    {
      label: '編輯',
      mnemonic: 'P',
      items: [
        { label: '放大字型', mnemonic: 'B', shortcut: 'Ctrl +', onSelect: () => setFontSize((f) => Math.min(40, f + 2)) },
        { label: '縮小字型', mnemonic: 'S', shortcut: 'Ctrl -', onSelect: () => setFontSize((f) => Math.max(8, f - 2)) },
        { label: '預設字型', mnemonic: '0', shortcut: 'Ctrl 0', onSelect: () => setFontSize(DEFAULT_FONT) },
        { label: '貼上範例', mnemonic: 'H', shortcut: 'Ctrl+H', onSelect: pasteSample },
      ] as MenuEntry[],
    },
    {
      label: '視窗',
      mnemonic: 'V',
      items: [
        { label: '顯示全部', mnemonic: 'A', onSelect: () => setShow({ statement: true, result: true, output: true }) },
        { label: '顯示題目', mnemonic: 'P', shortcut: 'Ctrl+P', onSelect: () => toggle('statement') },
        { label: '您的小黑', mnemonic: 'B', shortcut: 'Ctrl+B', disabled: true },
        { label: '標準小黑', mnemonic: 'T', shortcut: 'Ctrl+T', disabled: true },
        { label: '顯示結果', mnemonic: 'G', shortcut: 'Ctrl+G', onSelect: () => toggle('result') },
        { label: '您的輸出', mnemonic: 'J', shortcut: 'Ctrl+J', onSelect: () => (toggle('output', true), setOutputTab('mine')) },
        { label: '正確輸出', mnemonic: 'K', shortcut: 'Ctrl+K', onSelect: () => (toggle('output', true), setOutputTab('expected')) },
      ] as MenuEntry[],
    },
    { label: '編譯器', mnemonic: 'L', suffix: currentLang?.display ?? '', items: compilerItems },
    {
      label: '編譯測試',
      mnemonic: 'D',
      items: [
        { label: '題目預設測試資料', mnemonic: 'W', onSelect: () => runTests('sample') },
        { label: '一組隨機測試資料', mnemonic: 'E', disabled: true },
        { label: '十組隨機測試資料', mnemonic: 'C', disabled: true },
        { label: '使用自訂測試資料', mnemonic: 'D', onSelect: () => runTests('custom') },
        { label: '人工公開測試資料', mnemonic: 'S', onSelect: () => runTests('public') },
      ] as MenuEntry[],
    },
  ]

  // ───────── 右上角：倒數計時 / 碼錶 ─────────
  let timer: React.ReactNode
  if (mode === 'exam' && exam) {
    const rem = remainingMs(exam, now)
    timer = (
      <div className="solve-timer">
        {formatHms(rem)}
        <span className="apple">🍎</span>
        <div className="wf-progress" style={{ width: 100 }}>
          <div style={{ width: `${(rem / exam.durationMs) * 100}%` }} />
        </div>
      </div>
    )
  } else {
    const elapsed = (swPausedAt ?? now) - swStart
    timer = (
      <div className="solve-timer">
        ⏱ {formatHms(Math.max(0, elapsed))}
        <button
          className="wf-button"
          style={{ minWidth: 0 }}
          onClick={() => {
            if (swPausedAt === null) setSwPausedAt(Date.now())
            else {
              setSwStart((s) => s + (Date.now() - swPausedAt))
              setSwPausedAt(null)
            }
          }}
        >
          {swPausedAt === null ? '暫停' : '繼續'}
        </button>
        <button
          className="wf-button"
          style={{ minWidth: 0 }}
          onClick={() => {
            setSwStart(Date.now())
            setSwPausedAt(swPausedAt === null ? null : Date.now())
          }}
        >
          歸零
        </button>
      </div>
    )
  }

  const outputText = outputTab === 'mine' ? shown?.stdout : shown?.expected
  const outputLines = (outputText ?? '').replace(/\n$/, '').split('\n')
  const bodyRef = useRef<HTMLDivElement>(null)

  return (
    <Window title={`${code}評量:${problem.meta.title}`}>
      <MenuBar menus={menus} right={timer} />
      <div ref={bodyRef} style={{ flex: 1, minHeight: 0, display: 'flex', padding: 2 }}>
        <div style={{ flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column' }}>
          {show.statement && (
            <>
              <DockPane title="題文" onClose={() => toggle('statement', false)} style={{ height: statementH, flex: 'none' }}>
                <Statement html={problem.statement} />
              </DockPane>
              <Splitter direction="h" onDrag={(d) => setStatementH((h) => Math.max(60, h + d))} />
            </>
          )}
          <div className="wf-dock-pane" style={{ flex: 1 }}>
            {loaded && <CodeEditor value={source} onChange={setSource} lang={lang} fontSize={fontSize} />}
          </div>
          {show.output && (
            <>
              <Splitter direction="h" onDrag={(d) => setOutputH((h) => Math.max(60, h - d))} />
              <DockPane
                title={outputTab === 'mine' ? '您的輸出' : '正確輸出'}
                onClose={() => toggle('output', false)}
                style={{ height: outputH, flex: 'none' }}
                footer={
                  <div className="wf-doc-tabs">
                    <div className={'wf-doc-tab' + (outputTab === 'mine' ? ' active' : '')} onClick={() => setOutputTab('mine')}>
                      <span className="wf-tab-icon" />
                      您的輸出
                    </div>
                    <div className={'wf-doc-tab' + (outputTab === 'expected' ? ' active' : '')} onClick={() => setOutputTab('expected')}>
                      <span className="wf-tab-icon" />
                      正確輸出
                    </div>
                  </div>
                }
              >
                <div className="output-lines">
                  {outputText != null &&
                    outputLines.map((l, i) => (
                      <div key={i}>
                        <span className="ln">{i + 1}</span>
                        {l}
                      </div>
                    ))}
                </div>
              </DockPane>
            </>
          )}
        </div>
        {show.result && (
          <>
            <Splitter direction="v" onDrag={(d) => setRightW((w) => Math.max(220, w - d))} />
            <DockPane title="建置測試(G)" onClose={() => toggle('result', false)} style={{ width: rightW, flex: 'none' }}>
              <BuildPanel
                examinee={mode === 'exam' ? (session?.examinee ?? null) : null}
                badge={badge}
                words={words}
                chars={source.length}
                last={last}
                problemCode={code}
                problemTitle={problem.meta.title}
                compileMessage={compileMessage}
                input={input}
                onInputChange={setInput}
                shown={shown}
                caseSummary={caseSummary}
              />
            </DockPane>
          </>
        )}
      </div>
    </Window>
  )
}
