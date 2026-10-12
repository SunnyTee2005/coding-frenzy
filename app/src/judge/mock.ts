// 瀏覽器開發用的假後端（`npm run dev`）。
// - 考試狀態存在 localStorage，多個分頁（模擬多個視窗）會透過 storage 事件同步。
// - 判題規則：程式碼含 "CE" → COMPILER-ERROR，含 "WA" → WRONG-ANSWER，其餘 CORRECT。
import type { Backend } from './api'
import type { CodeDraft, ProblemDetail, SavedCode, Session, TestRun, Verdict } from './types'

const PROBLEMS: ProblemDetail[] = [
  ['272', 'TEX Quotes', 1, 26011, '輸入格式'],
  ['10035', 'Primary Arithmetic', 1, 26042, '算子運算'],
  ['948', 'Fibonaccimal Base', 1, 26064, '進制基底'],
  ['10189', 'Minesweeper', 1, 26071, '二維寫真'],
  ['10018', 'Reverse and Add', 1, 26081, '規則模擬'],
  ['10935', 'Throwing cards away I', 2, 26141, '堆疊佇列'],
  ['673', 'Parentheses Balance', 2, 26143, '堆疊佇列'],
].map(([id, title, stars, cpe26, category]) => ({
  meta: {
    id: String(id),
    title: String(title),
    stars: Number(stars),
    time_limit: 3,
    uva: Number(id),
    cpe26: Number(cpe26),
    category: String(category),
  },
  statement: `<h1>${title}</h1><h2>The Problem</h2><p>（mock 題目）</p><h2>Sample Input</h2><pre>1 2\n</pre><h2>Sample Output</h2><pre>3\n</pre>`,
}))

const KEY = 'cpe-sim-mock'
type Store = { session: Session; drafts: Record<string, CodeDraft>; saves: SavedCode[] }

function load(): Store {
  try {
    const raw = localStorage.getItem(KEY)
    if (raw) return JSON.parse(raw)
  } catch {
    // localStorage 不可用時用預設值
  }
  return { session: { phase: 'license', examinee: null, exam: null, practice: {} }, drafts: {}, saves: [] }
}

const listeners = new Set<(s: Session) => void>()

function save(store: Store) {
  try {
    localStorage.setItem(KEY, JSON.stringify(store))
  } catch {
    // 忽略
  }
  listeners.forEach((cb) => cb(store.session))
}

if (typeof window !== 'undefined') {
  window.addEventListener('storage', (e) => {
    if (e.key === KEY) listeners.forEach((cb) => cb(load().session))
  })
}

const delay = <T,>(value: T, ms = 120) => new Promise<T>((r) => setTimeout(() => r(value), ms))

function fakeVerdict(source: string): Verdict {
  if (source.includes('CE')) return 'COMPILER-ERROR'
  if (source.includes('WA')) return 'WRONG-ANSWER'
  return 'CORRECT'
}

function fakeRun(source: string, input: string): TestRun {
  const verdict = fakeVerdict(source)
  if (verdict === 'COMPILER-ERROR')
    return { verdict, compileMessage: "main.cpp:1:1: error: 'CE' does not name a type", cases: [] }
  return {
    verdict,
    compileMessage: null,
    cases: [
      {
        name: 'sample/1',
        verdict,
        input,
        expected: '3\n',
        stdout: verdict === 'CORRECT' ? '3\n' : '4\n',
        stderr: '',
        timeMs: 12,
        expectedTimeMs: 8,
      },
    ],
  }
}

export const mockBackend: Backend = {
  toolchainStatus: () =>
    delay({
      commandLineToolsInstalled: true,
      tools: [
        { lang_id: 'ccpp', display: 'CCPP:MinGW', program: '/usr/bin/clang++', version: 'mock' },
        { lang_id: 'python', display: 'PYTH:Python39', program: '/usr/bin/python3', version: 'mock' },
      ],
    }),
  installCommandLineTools: () => delay(undefined),
  languages: () =>
    delay([
      { id: 'ccpp', display: 'CCPP:MinGW', source: 'main.cpp' },
      { id: 'python', display: 'PYTH:Python39', source: 'main.py' },
    ]),
  problems: () => delay(PROBLEMS.map((p) => p.meta)),
  problem: (id) => delay(PROBLEMS.find((p) => p.meta.id === id) ?? PROBLEMS[0]),
  runTests: (_id, _lang, source) => delay(fakeRun(source, '1 2\n'), 400),
  runCustom: (_id, _lang, source, input) => delay(fakeRun(source, input), 400),
  formalJudge: (mode, id, _lang, source) => {
    const store = load()
    const verdict = fakeVerdict(source)
    const now = Date.now()
    let attempts = 1
    if (mode === 'exam' && store.session.exam) {
      const exam = store.session.exam
      if (exam.endedAtMs !== null || now >= exam.startedAtMs + exam.durationMs)
        return Promise.reject('考試時間已結束')
      const solved = exam.submissions.some((s) => s.problemId === id && s.verdict === 'CORRECT')
      if (!solved)
        exam.submissions.push({ problemId: id, atMs: now, minute: Math.floor((now - exam.startedAtMs) / 60000), verdict })
      attempts = exam.submissions.filter((s) => s.problemId === id).length
    } else {
      const rec = (store.session.practice[id] ??= { attempts: 0, solvedAtMs: null, lastVerdict: null })
      rec.attempts++
      rec.lastVerdict = verdict
      if (verdict === 'CORRECT' && rec.solvedAtMs === null) rec.solvedAtMs = now
      attempts = rec.attempts
    }
    save(store)
    return delay({ verdict, compileMessage: verdict === 'COMPILER-ERROR' ? 'error' : null, attempts }, 800)
  },

  sessionGet: () => delay({ session: load().session, nowMs: Date.now() }, 0),
  sessionAgreeLicense: () => {
    const store = load()
    if (store.session.phase === 'license') store.session.phase = 'login'
    save(store)
    return delay(undefined, 0)
  },
  sessionLogin: (idNo, ticket, problemIds) => {
    if (!idNo.trim() || !ticket.trim()) return Promise.reject('請填寫身分證字號與准考碼')
    const store = load()
    store.session.phase = 'exam'
    store.session.examinee = { idNo, ticket, name: '模擬考生', authCode: String(Date.now() % 1000000).padStart(6, '0') }
    store.session.exam = {
      code: '00A',
      startedAtMs: Date.now(),
      durationMs: 3 * 3600 * 1000,
      problems: problemIds.map((problemId, i) => ({ label: `00A${i + 1}`, problemId })),
      submissions: [],
      endedAtMs: null,
    }
    save(store)
    return delay(undefined, 0)
  },
  sessionEndExam: () => {
    const store = load()
    if (store.session.exam && store.session.exam.endedAtMs === null) store.session.exam.endedAtMs = Date.now()
    save(store)
    return delay(undefined, 0)
  },
  sessionReset: () => {
    const store = load()
    store.session = { phase: 'license', examinee: null, exam: null, practice: store.session.practice }
    save(store)
    return delay(undefined, 0)
  },
  onSessionChanged: (cb) => {
    listeners.add(cb)
    return Promise.resolve(() => listeners.delete(cb))
  },

  draftLoad: (scope, id) => delay(load().drafts[`${scope}-${id}`] ?? null, 0),
  draftSave: (scope, draft) => {
    const store = load()
    store.drafts[`${scope}-${draft.problemId}`] = draft
    try {
      localStorage.setItem(KEY, JSON.stringify(store))
    } catch {
      // 忽略
    }
    return delay(undefined, 0)
  },
  savesList: () => delay([...load().saves].sort((a, b) => b.createdAtMs - a.createdAtMs), 0),
  saveCode: (name, draft) => {
    const store = load()
    const saved = { ...draft, name, createdAtMs: Date.now() }
    store.saves.push(saved)
    save(store)
    return delay(saved, 0)
  },

  openSolveWindow: (mode, id) => {
    window.open(`${location.pathname}#/solve/${mode}/${id}`, `${mode}-${id}`)
    return Promise.resolve()
  },
  openToolWindow: (kind) => {
    window.open(`${location.pathname}#/${kind}`, kind)
    return Promise.resolve()
  },
}
