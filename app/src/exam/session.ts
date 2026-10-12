// 考試狀態的 React hook 與時間顯示格式。
// 所有格式都照考場截圖（見 docs/ui-spec.md）。

import { useEffect, useState } from 'react'
import { api } from '../judge/api'
import type { Exam, Session } from '../judge/types'

/** 取得考試狀態，並在任何視窗修改後自動更新。 */
export function useSession(): Session | null {
  const [session, setSession] = useState<Session | null>(null)
  useEffect(() => {
    let alive = true
    let unlisten: (() => void) | undefined
    api.sessionGet().then((v) => alive && setSession(v.session))
    api.onSessionChanged((s) => alive && setSession(s)).then((u) => (unlisten = u))
    return () => {
      alive = false
      unlisten?.()
    }
  }, [])
  return session
}

/** 每秒更新一次的現在時間。 */
export function useNow(intervalMs = 1000): number {
  const [now, setNow] = useState(() => Date.now())
  useEffect(() => {
    const t = setInterval(() => setNow(Date.now()), intervalMs)
    return () => clearInterval(t)
  }, [intervalMs])
  return now
}

export function remainingMs(exam: Exam, now: number): number {
  if (exam.endedAtMs !== null) return 0
  return Math.max(0, exam.startedAtMs + exam.durationMs - now)
}

export function isExamOver(exam: Exam, now: number): boolean {
  return remainingMs(exam, now) === 0
}

/** 解題視窗右上角：`2小時11分33秒` */
export function formatHms(ms: number): string {
  const total = Math.floor(ms / 1000)
  return `${Math.floor(total / 3600)}小時${Math.floor((total % 3600) / 60)}分${total % 60}秒`
}

/** 主畫面右上角：`剩151分45秒` */
export function formatRemainingShort(ms: number): string {
  const total = Math.floor(ms / 1000)
  return `剩${Math.floor(total / 60)}分${total % 60}秒`
}

const pad = (n: number) => String(n).padStart(2, '0')

/** `3月11日18:40` */
export function formatMonthDayHm(ms: number): string {
  const d = new Date(ms)
  return `${d.getMonth() + 1}月${d.getDate()}日${pad(d.getHours())}:${pad(d.getMinutes())}`
}

/** 主畫面工具列的現在時間：`3月11日19:09:14` */
export function formatMonthDayHms(ms: number): string {
  return `${formatMonthDayHm(ms)}:${pad(new Date(ms).getSeconds())}`
}

/** 題號：`00A1.UVA10035` */
export function problemCode(label: string, uva: number | null, id: string): string {
  return `${label}.UVA${uva ?? id}`
}
