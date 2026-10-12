// 前端呼叫後端的唯一入口。
// 在 Tauri 內走 invoke；用瀏覽器直接開 `npm run dev` 時改用 mock，方便做 UI 與 e2e 測試。
// 之後的網頁版可以在這裡換成 WASM 判題實作。

import { invoke } from '@tauri-apps/api/core'
import { listen } from '@tauri-apps/api/event'
import type {
  CodeDraft,
  FormalResult,
  Language,
  Mode,
  ProblemDetail,
  ProblemMeta,
  SavedCode,
  Session,
  SessionView,
  TestRun,
  TestSet,
  ToolchainReport,
} from './types'
import { mockBackend } from './mock'

export interface Backend {
  toolchainStatus(): Promise<ToolchainReport>
  installCommandLineTools(): Promise<void>
  languages(): Promise<Language[]>
  problems(): Promise<ProblemMeta[]>
  problem(id: string): Promise<ProblemDetail>
  /** 題目原文 PDF 的 bytes */
  problemPdf(id: string): Promise<ArrayBuffer>
  runTests(id: string, lang: string, source: string, set: TestSet): Promise<TestRun>
  runCustom(id: string, lang: string, source: string, input: string): Promise<TestRun>
  formalJudge(mode: Mode, id: string, lang: string, source: string): Promise<FormalResult>

  sessionGet(): Promise<SessionView>
  sessionAgreeLicense(): Promise<void>
  sessionLogin(idNo: string, ticket: string, problemIds: string[]): Promise<void>
  /** 預約下一場考試的題目並回到登入畫面 */
  sessionPlanExam(title: string, problemIds: string[]): Promise<void>
  sessionEndExam(): Promise<void>
  sessionReset(): Promise<void>
  onSessionChanged(cb: (s: Session) => void): Promise<() => void>

  draftLoad(scope: Mode, id: string): Promise<CodeDraft | null>
  draftSave(scope: Mode, draft: CodeDraft): Promise<void>
  savesList(): Promise<SavedCode[]>
  saveCode(name: string, draft: CodeDraft): Promise<SavedCode>

  openSolveWindow(mode: Mode | 'view', id: string, title: string): Promise<void>
  openToolWindow(kind: 'scoreboard' | 'practice' | 'cppref', title: string): Promise<void>
}

const tauriBackend: Backend = {
  toolchainStatus: () => invoke('toolchain_status'),
  installCommandLineTools: () => invoke('install_command_line_tools'),
  languages: () => invoke('languages'),
  problems: () => invoke('problems'),
  problem: (id) => invoke('problem', { id }),
  problemPdf: (id) => invoke<ArrayBuffer>('problem_pdf', { id }),
  runTests: (id, lang, source, set) => invoke('run_tests', { id, lang, source, set }),
  runCustom: (id, lang, source, input) => invoke('run_custom', { id, lang, source, input }),
  formalJudge: (mode, id, lang, source) => invoke('formal_judge', { mode, id, lang, source }),

  sessionGet: () => invoke('session_get'),
  sessionAgreeLicense: () => invoke('session_agree_license'),
  sessionLogin: (idNo, ticket, problemIds) => invoke('session_login', { idNo, ticket, problemIds }),
  sessionPlanExam: (title, problemIds) => invoke('session_plan_exam', { title, problemIds }),
  sessionEndExam: () => invoke('session_end_exam'),
  sessionReset: () => invoke('session_reset'),
  onSessionChanged: (cb) => listen<Session>('session-changed', (e) => cb(e.payload)),

  draftLoad: (scope, id) => invoke('draft_load', { scope, id }),
  draftSave: (scope, draft) => invoke('draft_save', { scope, draft }),
  savesList: () => invoke('saves_list'),
  saveCode: (name, draft) => invoke('save_code', { name, draft }),

  openSolveWindow: (mode, id, title) => invoke('open_solve_window', { mode, id, title }),
  openToolWindow: (kind, title) => invoke('open_tool_window', { kind, title }),
}

export const isTauri = typeof window !== 'undefined' && '__TAURI_INTERNALS__' in window

export const api: Backend = isTauri ? tauriBackend : mockBackend
