// 歷屆考題資料（tools/fetch_history.py 從 CPE 官方「歷次考題一覽」整理）與題型標籤。

import historyJson from '../../../data/history.json'
import tagsJson from '../../../data/tags.json'

export interface HistoryProblem {
  /** 題位 1~7 */
  pos: number
  uva: number
  /** 官方清單上的題名 */
  title: string
  /** 官方題名與編號對不上時，該 UVa 編號實際的題名 */
  uvaTitle: string | null
  submissions: number
  attempted: number
  solved: number
  /** 繳交答對率 % */
  rateSubmit: number
  /** 作答答對率 % */
  rateAttempt: number
  /** 考生答對率 %（答對人數 / 考生總人數） */
  rateAll: number
}

export interface HistoryExam {
  /** YYYY-MM-DD */
  date: string
  avgSolved: number
  problems: HistoryProblem[]
}

export const HISTORY: HistoryExam[] = historyJson as HistoryExam[]

const TAGS = (tagsJson as { names: string[]; tags: Record<string, string[]> }).tags
export const TAG_NAMES: string[] = (tagsJson as { names: string[] }).names

/** 題型標籤；沒有分類的題目回傳「未分類」。 */
export function tagsOf(uva: number | string): string[] {
  return TAGS[String(uva)] ?? ['未分類']
}

export function displayTitle(p: HistoryProblem): string {
  return p.uvaTitle ?? p.title
}

/** 2025-12-09 → 2025/12/09 */
export function formatDate(date: string): string {
  return date.replaceAll('-', '/')
}
