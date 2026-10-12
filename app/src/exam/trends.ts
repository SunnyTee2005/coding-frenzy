// 出題趨勢與預測（純函式，方便測試）。資料來自 data/history.json 與 data/tags.json。
//
// 預測只是依歷屆統計的推估，不代表實際出題。

import type { HistoryExam } from './history'

export const POSITIONS = [1, 2, 3, 4, 5, 6, 7]

/** 每場平均答對題數。 */
export function avgSolvedSeries(history: HistoryExam[]): { date: string; value: number }[] {
  return history.map((e) => ({ date: e.date, value: e.avgSolved }))
}

/** 各題位的平均考生答對率（%）。 */
export function positionRates(history: HistoryExam[]): { pos: number; mean: number; n: number }[] {
  return POSITIONS.map((pos) => {
    const v = history.flatMap((e) => e.problems.filter((p) => p.pos === pos).map((p) => p.rateAll))
    return { pos, mean: v.length ? v.reduce((a, b) => a + b, 0) / v.length : 0, n: v.length }
  })
}

/**
 * 題型 × 題位的出現比例：cells[tag][pos-1] = 該題位的題目中帶有這個標籤的比例（0~1）。
 * 一題可以有多個標籤，所以同一題位的比例加總可能超過 1。
 */
export function tagByPosition(history: HistoryExam[], tagsOf: (uva: number) => string[]) {
  const slots = POSITIONS.map((pos) => history.filter((e) => e.problems.some((p) => p.pos === pos)).length)
  const counts = new Map<string, number[]>()
  for (const e of history)
    for (const p of e.problems)
      for (const t of tagsOf(p.uva)) {
        const row = counts.get(t) ?? POSITIONS.map(() => 0)
        row[p.pos - 1]++
        counts.set(t, row)
      }
  const cells = new Map<string, number[]>()
  for (const [t, row] of counts) cells.set(t, row.map((c, i) => (slots[i] ? c / slots[i] : 0)))
  const total = new Map([...counts].map(([t, row]) => [t, row.reduce((a, b) => a + b, 0)]))
  return { cells, total }
}

/** 某題型在 `split` 之前與之後的出現比例（每題次），用來看近年上升或下降的題型。 */
export function tagShift(history: HistoryExam[], tagsOf: (uva: number) => string[], split: string) {
  const share = (exams: HistoryExam[]) => {
    const slots = exams.reduce((a, e) => a + e.problems.length, 0)
    const m = new Map<string, number>()
    for (const e of exams) for (const p of e.problems) for (const t of tagsOf(p.uva)) m.set(t, (m.get(t) ?? 0) + 1)
    return { m, slots }
  }
  const before = share(history.filter((e) => e.date < split))
  const after = share(history.filter((e) => e.date >= split))
  const tags = new Set([...before.m.keys(), ...after.m.keys()])
  return [...tags]
    .map((tag) => {
      const b = before.slots ? (before.m.get(tag) ?? 0) / before.slots : 0
      const a = after.slots ? (after.m.get(tag) ?? 0) / after.slots : 0
      return { tag, before: b, after: a, delta: a - b }
    })
    .sort((x, y) => y.delta - x.delta)
}

/** 重複出題：不同題目數、出現兩次以上的題目數、題次中屬於「舊題重出」的比例。 */
export function repeatStats(history: HistoryExam[]) {
  const seen = new Map<number, number>()
  let reused = 0
  let slots = 0
  for (const e of history)
    for (const p of e.problems) {
      slots++
      if (seen.has(p.uva)) reused++
      seen.set(p.uva, (seen.get(p.uva) ?? 0) + 1)
    }
  return {
    distinct: seen.size,
    repeated: [...seen.values()].filter((c) => c > 1).length,
    reuseRate: slots ? reused / slots : 0,
    slots,
  }
}

/** 年份差（以日期字串計算）。 */
function yearsBetween(a: string, b: string): number {
  return (new Date(b).getTime() - new Date(a).getTime()) / (365.25 * 24 * 3600 * 1000)
}

/**
 * 依時間加權的題型權重：越近的考試權重越高（半衰期 `halfLifeYears` 年）。
 * 回傳每個題位最常見的題型（權重由高到低，已正規化為比例）。
 */
export function weightedTagsByPosition(
  history: HistoryExam[],
  tagsOf: (uva: number) => string[],
  asOf: string,
  halfLifeYears = 3,
): { tag: string; weight: number }[][] {
  return POSITIONS.map((pos) => {
    const w = new Map<string, number>()
    let sum = 0
    for (const e of history) {
      const weight = Math.pow(0.5, yearsBetween(e.date, asOf) / halfLifeYears)
      for (const p of e.problems.filter((x) => x.pos === pos))
        for (const t of tagsOf(p.uva).filter((t) => t !== '未分類')) {
          w.set(t, (w.get(t) ?? 0) + weight)
          sum += weight
        }
    }
    return [...w]
      .map(([tag, v]) => ({ tag, weight: sum ? v / sum : 0 }))
      .sort((a, b) => b.weight - a.weight)
  })
}

/** 官方星等配置：前三題一顆星、P4~P5 兩顆星、P6 三顆星、P7 四顆星。 */
export const EXPECTED_STARS = [1, 1, 1, 2, 2, 3, 4]

export interface Candidate {
  id: string
  stars: number
  tags: string[]
}

export interface PredictedSlot {
  pos: number
  id: string
  reason: string
}

/**
 * 產生一份「預測模擬卷」：
 * - 第 1 題來自 CPE26 選集（2027 年起每場必有一題），優先選還沒考過的。
 * - 其餘題位依該題位近年最常見的題型，從題庫挑星等最接近、最近沒考過的題目。
 * 題目不重複；題庫不夠時用星等最接近的題目補。
 */
export function predictExam(opts: {
  history: HistoryExam[]
  bank: Candidate[]
  cpe26: Set<string>
  tagsOf: (uva: number) => string[]
  asOf: string
  random?: () => number
}): PredictedSlot[] {
  const { history, bank, cpe26, tagsOf, asOf } = opts
  const random = opts.random ?? Math.random
  const lastSeen = new Map<string, string>()
  for (const e of history) for (const p of e.problems) lastSeen.set(String(p.uva), e.date)
  const used = new Set<string>()
  const weights = weightedTagsByPosition(history, tagsOf, asOf)
  const slots: PredictedSlot[] = []

  // 打分：星等差越小越好，最近考過的扣分，加一點隨機避免每次都一樣
  const score = (c: Candidate, stars: number) => {
    const seen = lastSeen.get(c.id)
    const recency = seen ? Math.max(0, 3 - yearsBetween(seen, asOf)) : 0
    return Math.abs(c.stars - stars) * 10 + recency * 3 + random()
  }
  const best = (cands: Candidate[], stars: number) =>
    cands.filter((c) => !used.has(c.id)).sort((a, b) => score(a, stars) - score(b, stars))[0]

  const fromCpe26 = best(
    bank.filter((c) => cpe26.has(c.id)).sort((a, b) => Number(lastSeen.has(a.id)) - Number(lastSeen.has(b.id))),
    1,
  )
  const unseen26 = bank.filter((c) => cpe26.has(c.id) && !lastSeen.has(c.id) && !used.has(c.id))
  const first = unseen26.length ? unseen26[Math.floor(random() * unseen26.length)] : fromCpe26
  if (first) {
    used.add(first.id)
    slots.push({ pos: 1, id: first.id, reason: lastSeen.has(first.id) ? 'CPE26 選集' : 'CPE26 選集（歷屆未考過）' })
  }

  for (const pos of POSITIONS.slice(1)) {
    const stars = EXPECTED_STARS[pos - 1]
    let pick: Candidate | undefined
    let reason = ''
    for (const { tag, weight } of weights[pos - 1].slice(0, 5)) {
      pick = best(bank.filter((c) => c.tags.includes(tag)), stars)
      if (pick && Math.abs(pick.stars - stars) <= 1) {
        reason = `P${pos} 近年常見題型「${tag}」（${Math.round(weight * 100)}%）`
        break
      }
      pick = undefined
    }
    if (!pick) {
      pick = best(bank, stars)
      reason = `題庫中星等最接近 ${stars} 星的題目`
    }
    if (!pick) break
    used.add(pick.id)
    slots.push({ pos, id: pick.id, reason })
  }
  return slots
}
