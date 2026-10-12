import { describe, expect, it } from 'vitest'
import { compareScores, drawExam, elapsedMinutes, percentileFor, scoreExam } from './scoring'

describe('scoreExam', () => {
  it('matches the official ICPC example: 10 + 32 + 20×1 = 62', () => {
    // 開賽 10 分答對 A；15 分送出 B 錯誤；32 分答對 B。
    const score = scoreExam(
      ['A', 'B'],
      [
        { problemId: 'A', minute: 10, verdict: 'CORRECT' },
        { problemId: 'B', minute: 15, verdict: 'WRONG-ANSWER' },
        { problemId: 'B', minute: 32, verdict: 'CORRECT' },
      ],
    )
    expect(score.solved).toBe(2)
    expect(score.totalTime).toBe(62)
  })

  it('does not charge penalty for unsolved problems', () => {
    const score = scoreExam(
      ['A', 'B'],
      [
        { problemId: 'A', minute: 5, verdict: 'WRONG-ANSWER' },
        { problemId: 'A', minute: 6, verdict: 'RUN-ERROR' },
        { problemId: 'B', minute: 40, verdict: 'CORRECT' },
      ],
    )
    expect(score.solved).toBe(1)
    expect(score.totalTime).toBe(40)
    expect(score.problems[0]).toMatchObject({ solved: false, wrongAttempts: 2, time: 0 })
  })

  it('ignores submissions after the first correct one', () => {
    const score = scoreExam(
      ['A'],
      [
        { problemId: 'A', minute: 20, verdict: 'CORRECT' },
        { problemId: 'A', minute: 25, verdict: 'WRONG-ANSWER' },
      ],
    )
    expect(score.totalTime).toBe(20)
  })

  it('does not penalize compiler errors', () => {
    const score = scoreExam(
      ['A'],
      [
        { problemId: 'A', minute: 3, verdict: 'COMPILER-ERROR' },
        { problemId: 'A', minute: 8, verdict: 'CORRECT' },
      ],
    )
    expect(score.totalTime).toBe(8)
  })
})

describe('compareScores', () => {
  it('ranks by solved count, then total time', () => {
    const a = { solved: 3, totalTime: 300, problems: [] }
    const b = { solved: 2, totalTime: 10, problems: [] }
    const c = { solved: 3, totalTime: 100, problems: [] }
    expect([a, b, c].sort(compareScores)).toEqual([c, a, b])
  })
})

describe('elapsedMinutes', () => {
  it('truncates to whole minutes', () => {
    expect(elapsedMinutes(0, 59_999)).toBe(0)
    expect(elapsedMinutes(0, 60_000)).toBe(1)
    expect(elapsedMinutes(1000, 0)).toBe(0)
  })
})

describe('drawExam', () => {
  const bank = (counts: Record<number, number>) =>
    Object.entries(counts).flatMap(([stars, n]) =>
      Array.from({ length: n }, (_, i) => ({ id: `${stars}-${i}`, stars: Number(stars) })),
    )

  it('uses the 3/2/1/1 star layout when the bank is complete', () => {
    const picked = drawExam(bank({ 1: 10, 2: 10, 3: 10, 4: 10 }))
    expect(picked.map((p) => p.stars)).toEqual([1, 1, 1, 2, 2, 3, 4])
    expect(new Set(picked.map((p) => p.id)).size).toBe(7)
  })

  it('fills missing stars from lower levels first', () => {
    const picked = drawExam(bank({ 1: 49 }))
    expect(picked).toHaveLength(7)
    expect(picked.every((p) => p.stars === 1)).toBe(true)
  })

  it('returns fewer problems when the bank is too small', () => {
    expect(drawExam(bank({ 1: 2 }))).toHaveLength(2)
  })
})

describe('percentileFor', () => {
  it('maps solved counts onto the official 2022/3 distribution', () => {
    expect(percentileFor(0)).toBe(16.6)
    expect(percentileFor(2)).toBe(64.9)
    expect(percentileFor(7)).toBe(99.9)
    expect(percentileFor(9)).toBe(99.9)
  })

  it('increases with more problems solved', () => {
    for (let s = 1; s <= 7; s++) expect(percentileFor(s)).toBeGreaterThan(percentileFor(s - 1))
  })
})
