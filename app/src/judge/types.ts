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
export type Mode = 'exam' | 'practice'

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
  cpe26: number | null
  category: string | null
}

export interface ProblemDetail {
  meta: ProblemMeta
  /** HTML 片段 */
  statement: string
}

export interface TestCaseView {
  name: string
  verdict: Verdict
  input: string
  expected: string | null
  stdout: string
  stderr: string
  timeMs: number
  expectedTimeMs: number | null
}

export interface TestRun {
  verdict: Verdict
  compileMessage: string | null
  cases: TestCaseView[]
}

export interface FormalResult {
  verdict: Verdict
  compileMessage: string | null
  attempts: number
}

// ───────────── 考試狀態 ─────────────

export type Phase = 'license' | 'login' | 'exam'

export interface Examinee {
  idNo: string
  name: string
  ticket: string
  authCode: string
}

export interface ExamProblem {
  label: string
  problemId: string
}

export interface Submission {
  problemId: string
  atMs: number
  minute: number
  verdict: Verdict
}

export interface Exam {
  code: string
  startedAtMs: number
  durationMs: number
  problems: ExamProblem[]
  submissions: Submission[]
  endedAtMs: number | null
  /** 預約考卷的名稱（考古題、預測卷） */
  title: string | null
}

export interface PlannedExam {
  title: string
  problemIds: string[]
}

export interface PracticeRecord {
  attempts: number
  solvedAtMs: number | null
  lastVerdict: Verdict | null
}

export interface Session {
  phase: Phase
  examinee: Examinee | null
  exam: Exam | null
  practice: Record<string, PracticeRecord>
  planned: PlannedExam | null
}

export interface SessionView {
  session: Session
  nowMs: number
}

export interface CodeDraft {
  problemId: string
  lang: string
  source: string
}

export interface SavedCode extends CodeDraft {
  name: string
  createdAtMs: number
}
