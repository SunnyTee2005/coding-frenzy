import { describe, expect, it } from 'vitest'
import { formatHms, formatMonthDayHm, formatMonthDayHms, formatRemainingShort, problemCode, remainingMs } from './session'
import type { Exam } from '../judge/types'

const exam = (over: Partial<Exam> = {}): Exam => ({
  code: '00A',
  startedAtMs: 0,
  durationMs: 3 * 3600_000,
  problems: [],
  submissions: [],
  endedAtMs: null,
  title: null,
  ...over,
})

describe('time formats (as shown in the exam client)', () => {
  it('formats solve-window remaining time like 2小時11分33秒', () => {
    expect(formatHms((2 * 3600 + 11 * 60 + 33) * 1000 + 999)).toBe('2小時11分33秒')
    expect(formatHms(0)).toBe('0小時0分0秒')
  })

  it('formats main-window remaining time like 剩151分45秒', () => {
    expect(formatRemainingShort((151 * 60 + 45) * 1000)).toBe('剩151分45秒')
  })

  it('formats dates like 3月11日18:40 and 3月11日19:09:14', () => {
    const t = new Date(2026, 2, 11, 19, 9, 4).getTime()
    expect(formatMonthDayHm(t)).toBe('3月11日19:09')
    expect(formatMonthDayHms(t)).toBe('3月11日19:09:04')
  })

  it('builds problem codes like 00A1.UVA10035', () => {
    expect(problemCode('00A1', 10035, '10035')).toBe('00A1.UVA10035')
    expect(problemCode('00A2', null, '272')).toBe('00A2.UVA272')
  })
})

describe('remainingMs', () => {
  it('counts down from the start and stops at zero', () => {
    expect(remainingMs(exam(), 3600_000)).toBe(2 * 3600_000)
    expect(remainingMs(exam(), 4 * 3600_000)).toBe(0)
  })

  it('is zero once the exam was ended manually', () => {
    expect(remainingMs(exam({ endedAtMs: 10 }), 20)).toBe(0)
  })
})
