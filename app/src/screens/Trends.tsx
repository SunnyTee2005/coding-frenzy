// 出題趨勢（模擬器額外功能）：用 CPE 官方歷次考題統計觀察出題方向，並產生「預測模擬卷」。
// 圖表依 dataviz 規範：單一系列用藍色、熱度圖用單色藍色階、細線條、hover 提示、文字用中性色。
// 模擬器整體仿 Windows 淺色介面，所以只做淺色模式。

import { useMemo, useRef, useState } from 'react'
import { api } from '../judge/api'
import type { ProblemMeta } from '../judge/types'
import { CPE26 } from '../exam/cpe26'
import { HISTORY, formatDate, tagsOf } from '../exam/history'
import {
  EXPECTED_STARS,
  POSITIONS,
  avgSolvedSeries,
  positionRates,
  predictExam,
  repeatStats,
  tagByPosition,
  tagShift,
  weightedTagsByPosition,
  type PredictedSlot,
} from '../exam/trends'
import { useDialogs } from '../winforms/Dialogs'

const C = {
  text: '#0b0b0b',
  text2: '#52514e',
  muted: '#8a8984',
  grid: '#e6e5e1',
  series: '#2a78d6',
  surface: '#ffffff',
}
// 單色藍色階（100 → 700），熱度圖用
const RAMP = ['#cde2fb', '#b7d3f6', '#9ec5f4', '#86b6ef', '#6da7ec', '#5598e7', '#3987e5', '#2a78d6', '#256abf', '#1c5cab', '#184f95', '#104281', '#0d366b']

const TEN_YEARS = '2016-01-01'
const RECENT = '2023-01-01'

export function TrendsTab({ bank }: { bank: ProblemMeta[] }) {
  const dialogs = useDialogs()
  const recent10 = useMemo(() => HISTORY.filter((e) => e.date >= TEN_YEARS), [])
  const rates = useMemo(() => positionRates(recent10), [recent10])
  const repeat = useMemo(() => repeatStats(recent10), [recent10])
  const heat = useMemo(() => tagByPosition(recent10, tagsOf), [recent10])
  const shift = useMemo(() => tagShift(recent10, tagsOf, RECENT).filter((s) => s.tag !== '未分類'), [recent10])
  const [today] = useState(() => new Date().toISOString().slice(0, 10))
  const weights = useMemo(() => weightedTagsByPosition(recent10, tagsOf, today), [recent10, today])
  const [predicted, setPredicted] = useState<PredictedSlot[] | null>(null)

  const everSeen = new Set(HISTORY.flatMap((e) => e.problems.map((p) => p.uva)))
  const cpe26Seen = CPE26.filter((c) => everSeen.has(c.uva)).length
  const avg10 = recent10.reduce((a, e) => a + e.avgSolved, 0) / recent10.length
  const first3 = rates.slice(0, 3).reduce((a, r) => a + r.mean, 0) / 3

  const topTags = [...heat.total.entries()]
    .filter(([t]) => t !== '未分類')
    .sort((a, b) => b[1] - a[1])
    .slice(0, 12)
    .map(([t]) => t)

  const bankById = new Map(bank.map((p) => [p.id, p]))
  const predict = () =>
    setPredicted(
      predictExam({
        history: recent10,
        bank: bank.map((p) => ({ id: p.id, stars: p.stars, tags: tagsOf(p.id) })),
        cpe26: new Set(CPE26.map((c) => String(c.uva))),
        tagsOf,
        asOf: today,
      }),
    )

  const startPredicted = async () => {
    if (!predicted) return
    const ok = await dialogs.confirm('預測模擬卷', `要用這份 ${predicted.length} 題的預測卷開始 3 小時模擬考嗎？\n目前進行中的模擬考會被清除。`)
    if (!ok) return
    await api.sessionPlanExam('預測模擬卷', predicted.map((s) => s.id))
    await dialogs.message('預測模擬卷', '已設定考卷，請到主畫面登入，登入後立即開考。', { icon: 'info' })
  }

  return (
    <div style={{ fontFamily: 'var(--wf-font)', color: C.text, fontSize: 13 }}>
      <p style={{ marginTop: 0, color: C.text2 }}>
        資料：CPE 官方「歷次考題一覽」近十年 {recent10.length} 場（{formatDate(recent10[0].date)} ~ {formatDate(recent10[recent10.length - 1].date)}），題型為本模擬器人工標註。
        <b>以下預測只是依歷屆統計的推估，不是洩題。</b>
      </p>

      <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap', marginBottom: 18 }}>
        <Tile label="近十年平均答對題數" value={avg10.toFixed(2)} unit="題" />
        <Tile label="前三題平均考生答對率" value={first3.toFixed(1)} unit="%" />
        <Tile label="舊題重出比例" value={(repeat.reuseRate * 100).toFixed(1)} unit="%" note={`${repeat.slots} 題次中 ${repeat.repeated} 題出現兩次以上`} />
        <Tile label="CPE26 選集考過的題數" value={`${cpe26Seen}`} unit={`/ ${CPE26.length}`} note="2027 年起每場必有一題" />
      </div>

      <Section title="每場平均答對題數">
        <LineChart points={avgSolvedSeries(HISTORY).map((p) => ({ x: p.date, y: p.value }))} format={(v) => `${v.toFixed(2)} 題`} />
      </Section>

      <Section title="各題位的平均考生答對率（近十年）" note="官方把較簡單的三題排在前三題；後面的題目答對率急速下降。">
        <BarChart bars={rates.map((r) => ({ label: `P${r.pos}`, value: r.mean, sub: `${EXPECTED_STARS[r.pos - 1]}★ 參考` }))} format={(v) => `${v.toFixed(1)}%`} />
      </Section>

      <Section title="題型 × 題位（近十年，顏色越深代表該題位越常出這種題型）" note="一題可能有多個題型標籤。">
        <Heatmap rows={topTags} cells={heat.cells} />
      </Section>

      <Section title={`近年題型變化（${RECENT.slice(0, 4)} 年起 vs 之前）`}>
        <div style={{ display: 'flex', gap: 24, flexWrap: 'wrap' }}>
          <ShiftList title="比例上升" items={shift.filter((s) => s.delta > 0.002).slice(0, 6)} />
          <ShiftList title="比例下降" items={[...shift].reverse().filter((s) => s.delta < -0.002).slice(0, 6)} />
        </div>
      </Section>

      <Section title="下次考試預測">
        <table className="build-table" style={{ width: 'auto', marginBottom: 10 }}>
          <thead>
            <tr>
              {['題位', '參考星等', '近年最常見題型（近期權重較高）'].map((h) => (
                <th key={h} style={{ border: '1px solid #aaa', background: '#eee', padding: '2px 8px', textAlign: 'left' }}>
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {POSITIONS.map((pos) => (
              <tr key={pos}>
                <td>P{pos}</td>
                <td>{'★'.repeat(EXPECTED_STARS[pos - 1])}</td>
                <td style={{ color: C.text2 }}>
                  {pos === 1 && <b style={{ color: C.text }}>CPE26 選集一題（2027 起）；</b>}
                  {weights[pos - 1]
                    .slice(0, 3)
                    .map((w) => `${w.tag} ${Math.round(w.weight * 100)}%`)
                    .join('、')}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <button className="wf-button" onClick={predict} disabled={bank.length < 7}>
          產生預測模擬卷
        </button>{' '}
        {predicted && (
          <button className="wf-button" onClick={startPredicted}>
            用這份考卷開考
          </button>
        )}
        {bank.length < 7 && <span style={{ color: C.muted }}> 題庫少於 7 題，無法組卷。</span>}
        {predicted && (
          <table className="build-table" style={{ width: 'auto', marginTop: 10 }}>
            <tbody>
              {predicted.map((s) => {
                const m = bankById.get(s.id)
                return (
                  <tr key={s.pos}>
                    <td>P{s.pos}</td>
                    <td>UVA{s.id}</td>
                    <td>{m?.title}</td>
                    <td>{'★'.repeat(m?.stars ?? 0)}</td>
                    <td style={{ color: C.text2 }}>{s.reason}</td>
                    <td>
                      <a className="ie-link" onClick={() => api.openSolveWindow('practice', s.id, `PRAC.UVA${s.id}評量:${m?.title ?? ''}`)}>
                        練習
                      </a>
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        )}
      </Section>
    </div>
  )
}

function Section({ title, note, children }: { title: string; note?: string; children: React.ReactNode }) {
  return (
    <section style={{ marginBottom: 24 }}>
      <h3 style={{ margin: '0 0 2px', fontSize: 15 }}>{title}</h3>
      {note && <div style={{ color: C.text2, marginBottom: 6 }}>{note}</div>}
      {children}
    </section>
  )
}

function Tile({ label, value, unit, note }: { label: string; value: string; unit: string; note?: string }) {
  return (
    <div style={{ minWidth: 170, padding: '8px 12px', border: '1px solid #d6d5d0', background: '#fafaf8' }}>
      <div style={{ color: C.text2 }}>{label}</div>
      <div style={{ fontSize: 26, fontWeight: 'bold', fontVariantNumeric: 'tabular-nums' }}>
        {value}
        <span style={{ fontSize: 13, fontWeight: 'normal', color: C.text2 }}> {unit}</span>
      </div>
      {note && <div style={{ color: C.muted, fontSize: 12 }}>{note}</div>}
    </div>
  )
}

/** 浮動提示框：hover 時跟著滑鼠。 */
function useTooltip() {
  const [tip, setTip] = useState<{ x: number; y: number; text: string } | null>(null)
  const node = tip && (
    <div
      style={{
        position: 'absolute',
        left: tip.x + 12,
        top: tip.y - 30,
        padding: '3px 7px',
        background: '#fff',
        border: '1px solid #c9c8c3',
        boxShadow: '0 1px 4px rgba(0,0,0,.15)',
        color: C.text,
        fontSize: 12,
        whiteSpace: 'nowrap',
        pointerEvents: 'none',
      }}
    >
      {tip.text}
    </div>
  )
  return { setTip, node }
}

const W = 860
const H = 220
const PAD = { l: 36, r: 12, t: 12, b: 28 }

function LineChart({ points, format }: { points: { x: string; y: number }[]; format: (v: number) => string }) {
  const { setTip, node } = useTooltip()
  const [hover, setHover] = useState<number | null>(null)
  const box = useRef<HTMLDivElement>(null)
  const maxY = Math.ceil(Math.max(...points.map((p) => p.y)) * 2) / 2
  const xs = (i: number) => PAD.l + (i / (points.length - 1)) * (W - PAD.l - PAD.r)
  const ys = (v: number) => H - PAD.b - (v / maxY) * (H - PAD.t - PAD.b)
  const ticks = Array.from({ length: Math.round(maxY / 0.5) + 1 }, (_, i) => i * 0.5)
  // 每年第一場標年份；離上一個標籤太近（例如只有一場的年份）就略過，避免文字重疊
  const years: { i: number; y: string }[] = []
  points.forEach((p, i) => {
    const y = p.x.slice(0, 4)
    const last = years[years.length - 1]
    if ((!last || last.y !== y) && (!last || xs(i) - xs(last.i) >= 34)) years.push({ i, y })
  })

  return (
    <div ref={box} style={{ position: 'relative', maxWidth: W }}>
      <svg
        viewBox={`0 0 ${W} ${H}`}
        style={{ width: '100%', display: 'block' }}
        onMouseMove={(e) => {
          const r = (e.currentTarget as SVGSVGElement).getBoundingClientRect()
          const x = ((e.clientX - r.left) / r.width) * W
          const i = Math.max(0, Math.min(points.length - 1, Math.round(((x - PAD.l) / (W - PAD.l - PAD.r)) * (points.length - 1))))
          setHover(i)
          const br = box.current!.getBoundingClientRect()
          setTip({ x: e.clientX - br.left, y: e.clientY - br.top, text: `${formatDate(points[i].x)}：${format(points[i].y)}` })
        }}
        onMouseLeave={() => {
          setHover(null)
          setTip(null)
        }}
      >
        {ticks.map((t) => (
          <g key={t}>
            <line x1={PAD.l} x2={W - PAD.r} y1={ys(t)} y2={ys(t)} stroke={C.grid} />
            <text x={PAD.l - 6} y={ys(t) + 4} textAnchor="end" fontSize="11" fill={C.muted}>
              {t}
            </text>
          </g>
        ))}
        {years.map(({ i, y }) => (
          <text key={y} x={xs(i)} y={H - 8} fontSize="11" fill={C.muted} textAnchor="middle">
            {y}
          </text>
        ))}
        <polyline fill="none" stroke={C.series} strokeWidth="2" strokeLinejoin="round" points={points.map((p, i) => `${xs(i)},${ys(p.y)}`).join(' ')} />
        {hover !== null && (
          <>
            <line x1={xs(hover)} x2={xs(hover)} y1={PAD.t} y2={H - PAD.b} stroke={C.muted} strokeDasharray="3 3" />
            <circle cx={xs(hover)} cy={ys(points[hover].y)} r="5" fill={C.series} stroke={C.surface} strokeWidth="2" />
          </>
        )}
      </svg>
      {node}
    </div>
  )
}

function BarChart({ bars, format }: { bars: { label: string; value: number; sub: string }[]; format: (v: number) => string }) {
  const { setTip, node } = useTooltip()
  const box = useRef<HTMLDivElement>(null)
  const h = 200
  const max = Math.max(...bars.map((b) => b.value))
  const slot = (W - PAD.l - PAD.r) / bars.length
  const bw = Math.min(56, slot * 0.6)
  const ys = (v: number) => h - PAD.b - (v / max) * (h - PAD.t - PAD.b - 14)
  return (
    <div ref={box} style={{ position: 'relative', maxWidth: W }}>
      <svg viewBox={`0 0 ${W} ${h}`} style={{ width: '100%', display: 'block' }}>
        <line x1={PAD.l} x2={W - PAD.r} y1={h - PAD.b} y2={h - PAD.b} stroke={C.muted} />
        {bars.map((b, i) => {
          const x = PAD.l + i * slot + (slot - bw) / 2
          const y = ys(b.value)
          const height = h - PAD.b - y
          const r = Math.min(4, height / 2)
          return (
            <g
              key={b.label}
              onMouseMove={(e) => {
                const br = box.current!.getBoundingClientRect()
                setTip({ x: e.clientX - br.left, y: e.clientY - br.top, text: `${b.label}：${format(b.value)}（${b.sub}）` })
              }}
              onMouseLeave={() => setTip(null)}
            >
              {/* 比長條大的透明命中區 */}
              <rect x={PAD.l + i * slot} y={PAD.t} width={slot} height={h - PAD.t - PAD.b} fill="transparent" />
              <path
                d={`M${x},${h - PAD.b} V${y + r} Q${x},${y} ${x + r},${y} H${x + bw - r} Q${x + bw},${y} ${x + bw},${y + r} V${h - PAD.b} Z`}
                fill={C.series}
              />
              <text x={x + bw / 2} y={y - 5} textAnchor="middle" fontSize="12" fill={C.text}>
                {format(b.value)}
              </text>
              <text x={x + bw / 2} y={h - 10} textAnchor="middle" fontSize="12" fill={C.text2}>
                {b.label}
              </text>
            </g>
          )
        })}
      </svg>
      {node}
    </div>
  )
}

function Heatmap({ rows, cells }: { rows: string[]; cells: Map<string, number[]> }) {
  const { setTip, node } = useTooltip()
  const box = useRef<HTMLDivElement>(null)
  const max = Math.max(...rows.flatMap((t) => cells.get(t) ?? [0]))
  const color = (v: number) => (v <= 0 ? '#f3f3f1' : RAMP[Math.min(RAMP.length - 1, Math.floor((v / max) * (RAMP.length - 1)))])
  const cw = 64
  const ch = 22
  const lw = 96
  return (
    <div ref={box} style={{ position: 'relative', overflowX: 'auto' }}>
      <svg width={lw + cw * 7 + 4} height={ch * (rows.length + 1) + 4}>
        {POSITIONS.map((p, j) => (
          <text key={p} x={lw + j * cw + cw / 2} y={14} textAnchor="middle" fontSize="12" fill={C.text2}>
            P{p}
          </text>
        ))}
        {rows.map((tag, i) => (
          <g key={tag}>
            <text x={lw - 8} y={ch * (i + 1) + 15} textAnchor="end" fontSize="12" fill={C.text}>
              {tag}
            </text>
            {(cells.get(tag) ?? []).map((v, j) => (
              <rect
                key={j}
                x={lw + j * cw + 1}
                y={ch * (i + 1) + 1}
                width={cw - 2}
                height={ch - 2}
                rx="2"
                fill={color(v)}
                onMouseMove={(e) => {
                  const br = box.current!.getBoundingClientRect()
                  setTip({ x: e.clientX - br.left, y: e.clientY - br.top, text: `P${j + 1}「${tag}」：${(v * 100).toFixed(0)}% 的題目` })
                }}
                onMouseLeave={() => setTip(null)}
              />
            ))}
          </g>
        ))}
      </svg>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginTop: 4, color: C.text2, fontSize: 12 }}>
        少
        {RAMP.filter((_, i) => i % 2 === 0).map((c) => (
          <span key={c} style={{ display: 'inline-block', width: 18, height: 10, background: c }} />
        ))}
        多（最深 = {(max * 100).toFixed(0)}%）
      </div>
      {node}
    </div>
  )
}

function ShiftList({ title, items }: { title: string; items: { tag: string; before: number; after: number }[] }) {
  return (
    <div>
      <div style={{ fontWeight: 'bold', marginBottom: 4 }}>{title}</div>
      <table className="build-table" style={{ width: 'auto' }}>
        <tbody>
          {items.map((s) => (
            <tr key={s.tag}>
              <td>{s.tag}</td>
              <td style={{ color: C.text2, fontVariantNumeric: 'tabular-nums' }}>
                {(s.before * 100).toFixed(1)}% → <b style={{ color: C.text }}>{(s.after * 100).toFixed(1)}%</b>
              </td>
            </tr>
          ))}
          {items.length === 0 && (
            <tr>
              <td style={{ color: C.muted }}>（無明顯變化）</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  )
}
