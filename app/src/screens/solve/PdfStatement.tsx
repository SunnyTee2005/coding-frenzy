// 題文：和考場一樣直接顯示 UVa 原文 PDF（後端按需下載並快取，見 src-tauri/src/statements.rs）。
// 用 pdf.js 畫成 canvas，寬度貼齊面板；下載失敗時退回自寫的離線版題敘（若有）。

import { useEffect, useRef, useState } from 'react'
import * as pdfjs from 'pdfjs-dist/legacy/build/pdf.mjs'
import workerUrl from 'pdfjs-dist/legacy/build/pdf.worker.min.mjs?url'
import { api } from '../../judge/api'

pdfjs.GlobalWorkerOptions.workerSrc = workerUrl

type Doc = Awaited<ReturnType<typeof pdfjs.getDocument>['promise']>

export function PdfStatement({ problemId, fallbackHtml }: { problemId: string; fallbackHtml: string }) {
  const [doc, setDoc] = useState<Doc | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [width, setWidth] = useState(0)
  const box = useRef<HTMLDivElement>(null)
  const pages = useRef<HTMLDivElement>(null)

  useEffect(() => {
    // 每個解題視窗只顯示一題，problemId 不會改變，所以不需要重設狀態
    let alive = true
    api
      .problemPdf(problemId)
      .then((buf) => pdfjs.getDocument({ data: new Uint8Array(buf) }).promise)
      .then((d) => alive && setDoc(d))
      .catch((e) => alive && setError(String(e)))
    return () => {
      alive = false
    }
  }, [problemId])

  // 面板寬度改變時重畫（拖曳分隔線、縮放視窗）
  useEffect(() => {
    const el = box.current
    if (!el) return
    let t: ReturnType<typeof setTimeout> | undefined
    const ro = new ResizeObserver(() => {
      clearTimeout(t)
      t = setTimeout(() => setWidth(el.clientWidth), 120)
    })
    ro.observe(el)
    setWidth(el.clientWidth)
    return () => {
      ro.disconnect()
      clearTimeout(t)
    }
  }, [])

  useEffect(() => {
    if (!doc || !width || !pages.current) return
    let cancelled = false
    const host = pages.current
    ;(async () => {
      const ratio = window.devicePixelRatio || 1
      const canvases: HTMLCanvasElement[] = []
      for (let n = 1; n <= doc.numPages; n++) {
        const page = await doc.getPage(n)
        if (cancelled) return
        const base = page.getViewport({ scale: 1 })
        const scale = (width - 16) / base.width
        const vp = page.getViewport({ scale: scale * ratio })
        const canvas = document.createElement('canvas')
        canvas.width = Math.floor(vp.width)
        canvas.height = Math.floor(vp.height)
        canvas.style.width = `${Math.floor(vp.width / ratio)}px`
        canvas.style.display = 'block'
        canvas.style.margin = '0 auto 8px'
        await page.render({ canvasContext: canvas.getContext('2d')!, viewport: vp }).promise
        if (cancelled) return
        canvases.push(canvas)
      }
      host.replaceChildren(...canvases)
    })().catch((e) => !cancelled && setError(String(e)))
    return () => {
      cancelled = true
    }
  }, [doc, width])

  return (
    <div ref={box} style={{ minHeight: '100%', background: '#fff' }}>
      {error ? (
        fallbackHtml ? (
          <>
            <div className="sim-box" style={{ margin: 8 }}>
              <b>【模擬器】</b>無法下載題目原文 PDF，以下為離線版改寫題敘。
            </div>
            <div className="uva-statement" dangerouslySetInnerHTML={{ __html: fallbackHtml }} />
          </>
        ) : (
          <div className="sim-box" style={{ margin: 8, whiteSpace: 'pre-wrap' }}>
            <b>【模擬器】</b>題目原文 PDF 需要連網下載一次，之後離線也能看。{'\n'}
            {error}
          </div>
        )
      ) : (
        <>
          {!doc && <div style={{ padding: 12, color: '#666', fontFamily: 'var(--wf-font)' }}>題目下載中…</div>}
          <div ref={pages} style={{ paddingTop: 8 }} />
        </>
      )}
    </div>
  )
}
