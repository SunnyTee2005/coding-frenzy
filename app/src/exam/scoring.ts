// CPE 計分與抽題（ICPC 制）。
//
// - 先比答對題數，再比總時間（越少越好）。
// - 一題的時間 = 從開考到該題答對的分鐘數 + 該題答對前每次錯誤正式評判 × 20 分鐘。
// - 沒答對的題目不計時間、也不計罰時。
//
// TODO(Phase 0)：確認「看題不計時、按解題才計時」是否改變計時起點。

import type { Verdict } from '../judge/types'

export const PENALTY_MINUTES = 20

/** 一次正式評判。`minute` 是從開考起算的整數分鐘（無條件捨去）。 */
export interface Submission {
  problemId: string
  minute: number
  verdict: Verdict
}

export interface ProblemScore {
  problemId: string
  solved: boolean
  /** 答對時的分鐘數。 */
  solvedAt: number | null
  /** 答對前（或至今）錯誤的正式評判次數。 */
  wrongAttempts: number
  /** 這題計入總時間的分鐘數，沒答對為 0。 */
  time: number
}

export interface ExamScore {
  solved: number
  totalTime: number
  problems: ProblemScore[]
}

/** 從開考時間算出經過的整數分鐘。 */
export function elapsedMinutes(startMs: number, nowMs: number): number {
  return Math.max(0, Math.floor((nowMs - startMs) / 60_000))
}

export function scoreExam(problemIds: string[], submissions: Submission[]): ExamScore {
  const problems = problemIds.map((problemId): ProblemScore => {
    const subs = submissions
      .filter((s) => s.problemId === problemId)
      .sort((a, b) => a.minute - b.minute)
    let wrongAttempts = 0
    for (const s of subs) {
      if (s.verdict === 'CORRECT') {
        return {
          problemId,
          solved: true,
          solvedAt: s.minute,
          wrongAttempts,
          time: s.minute + wrongAttempts * PENALTY_MINUTES,
        }
      }
      // 編譯錯誤是否算罰時，待 Phase 0 對照原程式確認；目前比照 ICPC 慣例不計。
      if (s.verdict !== 'COMPILER-ERROR') wrongAttempts++
    }
    return { problemId, solved: false, solvedAt: null, wrongAttempts, time: 0 }
  })
  return {
    solved: problems.filter((p) => p.solved).length,
    totalTime: problems.reduce((sum, p) => sum + p.time, 0),
    problems,
  }
}

/** 排名比較：答對題數多者在前，同題數時總時間少者在前。 */
export function compareScores(a: ExamScore, b: ExamScore): number {
  return b.solved - a.solved || a.totalTime - b.totalTime
}

/** 每場考試的星等配置：3 題一顆星、2 題二顆星、1 題三顆星、1 題四顆星。 */
export const EXAM_LAYOUT: readonly number[] = [1, 1, 1, 2, 2, 3, 4]

/**
 * 依 EXAM_LAYOUT 抽題。某個星等的題目不夠時，用較低星等（再不夠就較高）的剩餘題目補上，
 * 讓題庫還不完整時也能組出 7 題。結果依星等排序。
 */
export function drawExam<T extends { id: string; stars: number }>(bank: T[], random: () => number = Math.random): T[] {
  const remaining = shuffle(bank, random)
  const picked: T[] = []
  for (const stars of EXAM_LAYOUT) {
    const order = [...remaining].sort(
      (a, b) => starDistance(a.stars, stars) - starDistance(b.stars, stars),
    )
    const choice = order[0]
    if (!choice) break
    picked.push(choice)
    remaining.splice(remaining.indexOf(choice), 1)
  }
  return picked.sort((a, b) => a.stars - b.stars)
}

// 同星等最優先，其次是較低星等，最後才是較高星等。
function starDistance(have: number, want: number): number {
  if (have === want) return 0
  return have < want ? want - have : 10 + have - want
}

function shuffle<T>(items: T[], random: () => number): T[] {
  const a = [...items]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}
