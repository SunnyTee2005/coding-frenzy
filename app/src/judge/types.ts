// 與 Rust 端（cpe-judge / src-tauri）序列化格式對應的型別。

export type Verdict =
  | 'CORRECT'
  | 'WRONG-ANSWER'
  | 'PRESENTATION-ERROR'
  | 'COMPILER-ERROR'
  | 'RUN-ERROR'
  | 'NO-OUTPUT'
  | 'TIMELIMIT'
  | 'PENDING'

export type TestSet = 'sample' | 'public'

export interface Language {
  id: string
  display: string
  source: string
}

export interface ToolStatus {
  lang_id: string
  display: string
  program: string | null
  version: string | null
}

export interface ToolchainReport {
  commandLineToolsInstalled: boolean
  tools: ToolStatus[]
}

export interface ProblemMeta {
  id: string
  title: string
  stars: number
  time_limit: number
  uva: number | null
}

export interface ProblemDetail {
  meta: ProblemMeta
  statement: string
  samples: { input: string; output: string }[]
}

export interface CaseResult {
  name: string
  verdict: Verdict
  time_ms: number
  memory_kb: number | null
  stdout: string
  stderr: string
  exit_code: number | null
}

export interface JudgeReport {
  verdict: Verdict
  compile_message: string | null
  cases: CaseResult[]
}

export type ProcStatus =
  | { Exited: number }
  | { Signaled: number }
  | 'TimedOut'
  | 'OutputLimit'

export interface CustomRun {
  compileMessage: string | null
  status: ProcStatus | null
  stdout: string
  stderr: string
  timeMs: number
}

export interface FormalResult {
  verdict: Verdict
  compileMessage: string | null
  timeMs: number
}
