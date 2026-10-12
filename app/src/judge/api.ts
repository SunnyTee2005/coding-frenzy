// 前端呼叫判題後端的唯一入口。
// 在 Tauri 內走 invoke；用瀏覽器直接開 `npm run dev` 時改用 mock，方便做 UI 與 e2e 測試。
// 之後的網頁版可以在這裡換成 WASM 判題實作。

import { invoke } from '@tauri-apps/api/core'
import type {
  CustomRun,
  FormalResult,
  JudgeReport,
  Language,
  ProblemDetail,
  ProblemMeta,
  TestSet,
  ToolchainReport,
} from './types'
import { mockBackend } from './mock'

export interface JudgeApi {
  toolchainStatus(): Promise<ToolchainReport>
  installCommandLineTools(): Promise<void>
  languages(): Promise<Language[]>
  problems(): Promise<ProblemMeta[]>
  problem(id: string): Promise<ProblemDetail>
  runTests(id: string, lang: string, source: string, set: TestSet): Promise<JudgeReport>
  runCustom(id: string, lang: string, source: string, input: string): Promise<CustomRun>
  formalJudge(id: string, lang: string, source: string): Promise<FormalResult>
}

const tauriBackend: JudgeApi = {
  toolchainStatus: () => invoke('toolchain_status'),
  installCommandLineTools: () => invoke('install_command_line_tools'),
  languages: () => invoke('languages'),
  problems: () => invoke('problems'),
  problem: (id) => invoke('problem', { id }),
  runTests: (id, lang, source, set) => invoke('run_tests', { id, lang, source, set }),
  runCustom: (id, lang, source, input) => invoke('run_custom', { id, lang, source, input }),
  formalJudge: (id, lang, source) => invoke('formal_judge', { id, lang, source }),
}

export const isTauri = typeof window !== 'undefined' && '__TAURI_INTERNALS__' in window

export const api: JudgeApi = isTauri ? tauriBackend : mockBackend
