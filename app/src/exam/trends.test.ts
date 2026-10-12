import { describe, expect, it } from 'vitest'
import type { HistoryExam, HistoryProblem } from './history'
import { positionRates, predictExam, repeatStats, tagByPosition, tagShift, weightedTagsByPosition } from './trends'

const prob = (pos: number, uva: number, rateAll: number): HistoryProblem => ({
  pos,
  uva,
  title: `T${uva}`,
  uvaTitle: null,
  submissions: 1,
  attempted: 1,
  solved: 1,
  rateSubmit: 1,
  rateAttempt: 1,
  rateAll,
})

const HIST: HistoryExam[] = [
  { date: '2020-03-01', avgSolved: 1, problems: [prob(1, 100, 60), prob(2, 200, 30)] },
  { date: '2024-03-01', avgSolved: 2, problems: [prob(1, 101, 40), prob(2, 100, 10)] },
]
const TAGS: Record<number, string[]> = { 100: ['字串'], 101: ['數學'], 200: ['字串', '排序'] }
const tagsOf = (u: number) => TAGS[u] ?? ['未分類']

describe('positionRates', () => {
  it('averages the solve rate per position', () => {
    const r = positionRates(HIST)
    expect(r[0]).toMatchObject({ pos: 1, mean: 50, n: 2 })
    expect(r[1]).toMatchObject({ pos: 2, mean: 20, n: 2 })
    expect(r[2]).toMatchObject({ pos: 3, n: 0 })
  })
})

describe('tagByPosition / tagShift', () => {
  it('computes the share of slots per tag and position', () => {
    const { cells, total } = tagByPosition(HIST, tagsOf)
    expect(cells.get('字串')).toEqual([0.5, 1, 0, 0, 0, 0, 0])
    expect(total.get('字串')).toBe(3)
  })

  it('reports tags gaining share after the split date', () => {
    const shift = tagShift(HIST, tagsOf, '2022-01-01')
    expect(shift[0].tag).toBe('數學')
    expect(shift.find((s) => s.tag === '排序')!.delta).toBeLessThan(0)
  })
})

describe('repeatStats', () => {
  it('counts problems that came back', () => {
    expect(repeatStats(HIST)).toEqual({ distinct: 3, repeated: 1, reuseRate: 0.25, slots: 4 })
  })
})

describe('weightedTagsByPosition', () => {
  it('weights recent exams more and normalizes', () => {
    const w = weightedTagsByPosition(HIST, tagsOf, '2024-06-01')
    expect(w[0][0].tag).toBe('數學')
    expect(w[0].reduce((a, b) => a + b.weight, 0)).toBeCloseTo(1)
  })
})

describe('predictExam', () => {
  const bank = [
    { id: '272', stars: 1, tags: ['字串'] },
    { id: '948', stars: 1, tags: ['進制'] },
    { id: '100', stars: 1, tags: ['字串'] },
    { id: '101', stars: 1, tags: ['數學'] },
    { id: '200', stars: 2, tags: ['字串', '排序'] },
    { id: '10189', stars: 2, tags: ['模擬'] },
    { id: '673', stars: 2, tags: ['資料結構'] },
    { id: '999', stars: 4, tags: ['圖論'] },
  ]
  const run = (seed: number) => {
    let s = seed
    const random = () => ((s = (s * 9301 + 49297) % 233280) / 233280)
    return predictExam({ history: HIST, bank, cpe26: new Set(['272', '948']), tagsOf, asOf: '2026-10-12', random })
  }

  it('always starts with a CPE26 problem and never repeats a problem', () => {
    for (let seed = 1; seed < 30; seed++) {
      const slots = run(seed)
      expect(['272', '948']).toContain(slots[0].id)
      expect(new Set(slots.map((s) => s.id)).size).toBe(slots.length)
      expect(slots.map((s) => s.pos)).toEqual(slots.map((_, i) => i + 1))
    }
  })

  it('fills all seven positions when the bank is large enough', () => {
    expect(run(7)).toHaveLength(7)
  })
})
