// WinForms 樣式的選單列。
// - Alt+字母：開啟對應選單，或直接執行沒有子選單的項目（例如 Alt+J 正式評判）。
// - 選單開啟時按字母選擇項目；Esc 關閉。
// - 項目上標示的快捷鍵（Ctrl+W、Ctrl + …）全域有效，搶在編輯器之前處理。

import { useEffect, useLayoutEffect, useRef, useState, type ReactNode } from 'react'

export type MenuEntry =
  | { sep: true }
  | {
      sep?: false
      label: string
      mnemonic?: string
      /** 接在助記鍵後面的文字，例如「考生手冊(H)(Handouts)」的 (Handouts) */
      after?: string
      shortcut?: string
      disabled?: boolean
      checked?: boolean
      icon?: ReactNode
      onSelect?: () => void
    }

export interface RootMenu {
  label: string
  mnemonic?: string
  /** 顯示在助記鍵後面的文字，例如「編譯器(L)CCPP:MinGW」的 CCPP:MinGW */
  suffix?: string
  items?: MenuEntry[]
  onSelect?: () => void
  bold?: boolean
  boxed?: boolean
  disabled?: boolean
}

const withMnemonic = (label: string, m?: string) => (m ? `${label}(${m})` : label)

/** 用 KeyboardEvent.code 比對，避免 Mac 上 Option+字母變成特殊符號。 */
function codeFor(ch: string): string {
  if (/^[a-z]$/i.test(ch)) return `Key${ch.toUpperCase()}`
  if (/^[0-9]$/.test(ch)) return `Digit${ch}`
  if (ch === '+' || ch === '=') return 'Equal'
  if (ch === '-') return 'Minus'
  return ch
}

/** 解析「Ctrl+W」「Ctrl +」「Ctrl 0」這類標示。 */
export function parseShortcut(s: string): { ctrl: boolean; code: string } | null {
  const m = /^Ctrl\s*\+?\s*(.)$/i.exec(s.trim())
  return m ? { ctrl: true, code: codeFor(m[1]) } : null
}

function matches(e: KeyboardEvent, shortcut?: string): boolean {
  if (!shortcut) return false
  const p = parseShortcut(shortcut)
  if (!p) return false
  const codeOk = e.code === p.code || (p.code === 'Equal' && e.code === 'NumpadAdd') || (p.code === 'Minus' && e.code === 'NumpadSubtract')
  return codeOk && e.ctrlKey && !e.altKey && !e.metaKey
}

export function MenuBar({ menus, right }: { menus: RootMenu[]; right?: ReactNode }) {
  const [open, setOpen] = useState<number | null>(null)
  const barRef = useRef<HTMLDivElement>(null)
  // 鍵盤處理器只註冊一次，透過 ref 讀最新的選單與開啟狀態
  const menusRef = useRef(menus)
  const openRef = useRef(open)
  useLayoutEffect(() => {
    menusRef.current = menus
    openRef.current = open
  })

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const ms = menusRef.current
      // 全域快捷鍵
      for (const m of ms) {
        for (const it of m.items ?? []) {
          if (!it.sep && !it.disabled && matches(e, it.shortcut)) {
            e.preventDefault()
            e.stopPropagation()
            setOpen(null)
            it.onSelect?.()
            return
          }
        }
      }
      // Alt+助記鍵
      if (e.altKey && !e.ctrlKey && !e.metaKey) {
        const idx = ms.findIndex((m) => m.mnemonic && e.code === codeFor(m.mnemonic))
        if (idx >= 0) {
          e.preventDefault()
          e.stopPropagation()
          const m = ms[idx]
          if (m.disabled) return
          if (m.items) setOpen(idx)
          else {
            setOpen(null)
            m.onSelect?.()
          }
        }
        return
      }
      const cur = openRef.current
      if (cur === null) return
      if (e.key === 'Escape') {
        e.preventDefault()
        setOpen(null)
        return
      }
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        e.preventDefault()
        const step = e.key === 'ArrowRight' ? 1 : -1
        setOpen((cur + step + ms.length) % ms.length)
        return
      }
      const it = ms[cur].items?.find((x) => !x.sep && !x.disabled && x.mnemonic && e.code === codeFor(x.mnemonic))
      if (it && !it.sep) {
        e.preventDefault()
        e.stopPropagation()
        setOpen(null)
        it.onSelect?.()
      }
    }
    window.addEventListener('keydown', onKey, true)
    return () => window.removeEventListener('keydown', onKey, true)
  }, [])

  useEffect(() => {
    if (open === null) return
    const onDown = (e: MouseEvent) => {
      if (!barRef.current?.contains(e.target as Node)) setOpen(null)
    }
    window.addEventListener('mousedown', onDown)
    return () => window.removeEventListener('mousedown', onDown)
  }, [open])

  return (
    <div className="wf-menubar" ref={barRef}>
      <div className="wf-grip" />
      {menus.map((m, i) => (
        <div
          key={m.label}
          className={['wf-menu-root', m.bold && 'bold', m.boxed && 'boxed', open === i && 'open', m.disabled && 'disabled']
            .filter(Boolean)
            .join(' ')}
          onMouseDown={(e) => {
            if (m.disabled || e.button !== 0) return
            if (m.items) setOpen(open === i ? null : i)
            else {
              setOpen(null)
              m.onSelect?.()
            }
          }}
          onMouseEnter={() => open !== null && m.items && setOpen(i)}
        >
          {withMnemonic(m.label, m.mnemonic)}
          {m.suffix}
          {open === i && m.items && (
            <div className="wf-dropdown" onMouseDown={(e) => e.stopPropagation()}>
              {m.items.map((it, j) =>
                it.sep ? (
                  <div key={j} className="wf-menu-sep" />
                ) : (
                  <div
                    key={j}
                    className={'wf-menu-item' + (it.disabled ? ' disabled' : '')}
                    onClick={() => {
                      if (it.disabled) return
                      setOpen(null)
                      it.onSelect?.()
                    }}
                  >
                    <span className="wf-check">{it.checked ? '✔' : it.icon}</span>
                    {withMnemonic(it.label, it.mnemonic)}
                    {it.after}
                    {it.shortcut && <span className="wf-shortcut">{it.shortcut}</span>}
                  </div>
                ),
              )}
            </div>
          )}
        </div>
      ))}
      {right}
    </div>
  )
}
