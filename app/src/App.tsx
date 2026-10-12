// 暫時的「環境檢查」畫面：確認編譯器可用、判題後端正常。
// 真正的考場畫面要等 Phase 0 取得原程式的 UI 規格（docs/ui-spec）後再依規格實作，避免憑印象做出不像的版面。

import { useCallback, useEffect, useState } from 'react'
import { api, isTauri } from './judge/api'
import type { Language, ProblemMeta, ToolchainReport } from './judge/types'

const TEMPLATE: Record<string, string> = {
  ccpp: '#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {\n    long long a, b;\n    while (cin >> a >> b) cout << llabs(a - b) << "\\n";\n}\n',
  python: 'import sys\n\nfor line in sys.stdin:\n    a, b = map(int, line.split())\n    print(abs(a - b))\n',
}

export default function App() {
  const [toolchain, setToolchain] = useState<ToolchainReport | null>(null)
  const [installing, setInstalling] = useState(false)
  const [languages, setLanguages] = useState<Language[]>([])
  const [problems, setProblems] = useState<ProblemMeta[]>([])
  const [problemId, setProblemId] = useState('')
  const [lang, setLang] = useState('ccpp')
  const [source, setSource] = useState(TEMPLATE.ccpp)
  const [result, setResult] = useState('')
  const [busy, setBusy] = useState(false)

  const refreshToolchain = useCallback(() => api.toolchainStatus().then(setToolchain), [])

  useEffect(() => {
    refreshToolchain()
    api.languages().then(setLanguages)
    api.problems().then((ps) => {
      setProblems(ps)
      if (ps[0]) setProblemId(ps[0].id)
    })
  }, [refreshToolchain])

  // 等待 Xcode Command Line Tools 安裝完成
  useEffect(() => {
    if (!installing) return
    const timer = setInterval(async () => {
      const report = await api.toolchainStatus()
      setToolchain(report)
      if (report.commandLineToolsInstalled) setInstalling(false)
    }, 3000)
    return () => clearInterval(timer)
  }, [installing])

  const run = async (action: () => Promise<string>) => {
    setBusy(true)
    setResult('評判中…')
    try {
      setResult(await action())
    } catch (e) {
      setResult(`錯誤：${e}`)
    } finally {
      setBusy(false)
    }
  }

  const runTests = (set: 'sample' | 'public') =>
    run(async () => {
      const r = await api.runTests(problemId, lang, source, set)
      if (r.compile_message) return `${r.verdict}\n\n${r.compile_message}`
      return [r.verdict, ...r.cases.map((c) => `${c.name.padEnd(12)} ${c.verdict.padEnd(20)} ${c.time_ms} ms`)].join('\n')
    })

  const formal = () =>
    run(async () => {
      const r = await api.formalJudge(problemId, lang, source)
      return r.compileMessage ? `${r.verdict}\n\n${r.compileMessage}` : `${r.verdict}（最慢 ${r.timeMs} ms）`
    })

  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', padding: 16, display: 'grid', gap: 12 }}>
      <h1 style={{ margin: 0, fontSize: 20 }}>CPE 模擬考場（非官方）— 環境檢查</h1>
      {!isTauri && <p style={{ color: '#a60' }}>目前在瀏覽器中執行，判題結果來自 mock 後端。</p>}

      <section>
        <h2 style={{ fontSize: 16 }}>編譯器</h2>
        {toolchain && !toolchain.commandLineToolsInstalled && (
          <p>
            尚未安裝 Xcode Command Line Tools（提供 C/C++ 編譯器與 Python 3）。{' '}
            <button
              disabled={installing}
              onClick={() => api.installCommandLineTools().then(() => setInstalling(true))}
            >
              {installing ? '安裝中，請依系統視窗指示完成…' : '安裝'}
            </button>
          </p>
        )}
        <ul>
          {toolchain?.tools.map((t) => (
            <li key={t.lang_id}>
              {t.display}：{t.program ? `${t.program}（${t.version ?? '版本不明'}）` : '找不到'}
            </li>
          ))}
        </ul>
      </section>

      <section style={{ display: 'flex', gap: 8, alignItems: 'center', flexWrap: 'wrap' }}>
        <select value={problemId} onChange={(e) => setProblemId(e.target.value)}>
          {problems.map((p) => (
            <option key={p.id} value={p.id}>
              {p.id} {p.title} {'★'.repeat(p.stars)}
            </option>
          ))}
        </select>
        <select
          value={lang}
          onChange={(e) => {
            setLang(e.target.value)
            setSource(TEMPLATE[e.target.value] ?? '')
          }}
        >
          {languages.map((l) => (
            <option key={l.id} value={l.id}>
              {l.display}
            </option>
          ))}
        </select>
        <button disabled={busy || !problemId} onClick={() => runTests('sample')}>
          題目預設測試資料
        </button>
        <button disabled={busy || !problemId} onClick={() => runTests('public')}>
          人工公開測試資料
        </button>
        <button disabled={busy || !problemId} onClick={formal}>
          正式評判
        </button>
      </section>

      <textarea
        value={source}
        onChange={(e) => setSource(e.target.value)}
        spellCheck={false}
        style={{ fontFamily: 'ui-monospace, Menlo, Consolas, monospace', fontSize: 14, height: 280 }}
      />
      <pre style={{ background: '#f4f4f4', padding: 8, minHeight: 80, whiteSpace: 'pre-wrap' }}>{result}</pre>
    </main>
  )
}
