// WinForms 樣式的對話框：訊息框、輸入框（另存新檔）、清單（提檔續答）。
// 用 Promise 介面：`await dialogs.confirm(...)`。

import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState, type ReactNode } from 'react'
import { TitleBar } from './Window'

type DialogSpec =
  | { kind: 'message'; title: string; text: string; icon?: 'question' | 'info'; buttons: string[]; defaultIndex?: number }
  | { kind: 'prompt'; title: string; label: string; value: string }
  | { kind: 'list'; title: string; items: string[] }

interface Pending {
  spec: DialogSpec
  resolve: (v: number | string | null) => void
}

interface DialogApi {
  /** 回傳按下的按鈕索引；關閉視窗回傳 -1。 */
  message(title: string, text: string, opts?: { icon?: 'question' | 'info'; buttons?: string[]; defaultIndex?: number }): Promise<number>
  /** 「是(Y) / 否(N)」，回傳是否按下「是」。 */
  confirm(title: string, text: string): Promise<boolean>
  prompt(title: string, label: string, value?: string): Promise<string | null>
  /** 回傳選取的索引；取消回傳 null。 */
  pickFromList(title: string, items: string[]): Promise<number | null>
}

const Ctx = createContext<DialogApi | null>(null)

export function useDialogs(): DialogApi {
  const ctx = useContext(Ctx)
  if (!ctx) throw new Error('useDialogs 必須在 DialogHost 內使用')
  return ctx
}

export function DialogHost({ children }: { children: ReactNode }) {
  const [pending, setPending] = useState<Pending | null>(null)

  const open = useCallback(
    (spec: DialogSpec) => new Promise<number | string | null>((resolve) => setPending({ spec, resolve })),
    [],
  )

  const api = useMemo<DialogApi>(
    () => ({
    message: async (title, text, opts) =>
      (await open({ kind: 'message', title, text, icon: opts?.icon, buttons: opts?.buttons ?? ['確定'], defaultIndex: opts?.defaultIndex ?? 0 })) as number,
    confirm: async (title, text) =>
      (await open({ kind: 'message', title, text, icon: 'question', buttons: ['是(Y)', '否(N)'], defaultIndex: 0 })) === 0,
    prompt: async (title, label, value = '') => (await open({ kind: 'prompt', title, label, value })) as string | null,
    pickFromList: async (title, items) => (await open({ kind: 'list', title, items })) as number | null,
    }),
    [open],
  )

  const close = (v: number | string | null) => {
    pending?.resolve(v)
    setPending(null)
  }

  return (
    <Ctx.Provider value={api}>
      {children}
      {pending && <DialogView spec={pending.spec} close={close} />}
    </Ctx.Provider>
  )
}

function DialogView({ spec, close }: { spec: DialogSpec; close: (v: number | string | null) => void }) {
  const [text, setText] = useState(spec.kind === 'prompt' ? spec.value : '')
  const [selected, setSelected] = useState(0)
  const defaultRef = useRef<HTMLButtonElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)
  const cancelValue = spec.kind === 'message' ? -1 : null

  useEffect(() => {
    if (spec.kind === 'prompt') inputRef.current?.select()
    else defaultRef.current?.focus()
  }, [spec.kind])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault()
        e.stopPropagation()
        close(cancelValue)
      }
      // 「是(Y)」「否(N)」的助記鍵
      if (spec.kind === 'message' && !e.ctrlKey && !e.metaKey) {
        const idx = spec.buttons.findIndex((b) => b.toUpperCase().includes(`(${e.key.toUpperCase()})`))
        if (idx >= 0) {
          e.preventDefault()
          e.stopPropagation()
          close(idx)
        }
      }
    }
    window.addEventListener('keydown', onKey, true)
    return () => window.removeEventListener('keydown', onKey, true)
  })

  return (
    <div className="wf-modal-backdrop" onMouseDown={(e) => e.stopPropagation()}>
      <div className="wf-dialog" role="dialog" aria-label={spec.title}>
        <TitleBar title={spec.title} onClose={() => close(cancelValue)} closeOnly={spec.kind === 'message'} inDialog />
        {spec.kind === 'message' && (
          <>
            <div className="wf-dialog-content" style={{ maxWidth: 520 }}>
              {spec.icon && <div className="wf-icon-question">{spec.icon === 'question' ? '?' : 'i'}</div>}
              <div style={{ whiteSpace: 'pre-wrap' }}>{spec.text}</div>
            </div>
            <div className="wf-dialog-buttons">
              {spec.buttons.map((b, i) => (
                <button
                  key={b}
                  ref={i === spec.defaultIndex ? defaultRef : undefined}
                  className={'wf-button' + (i === spec.defaultIndex ? ' default' : '')}
                  onClick={() => close(i)}
                >
                  {b}
                </button>
              ))}
            </div>
          </>
        )}
        {spec.kind === 'prompt' && (
          <form
            onSubmit={(e) => {
              e.preventDefault()
              close(text)
            }}
            style={{ width: 500, padding: '18px 22px 16px' }}
          >
            <div style={{ marginBottom: 14 }}>{spec.label}</div>
            <input ref={inputRef} className="wf-textbox" style={{ width: '100%', height: 24 }} value={text} onChange={(e) => setText(e.target.value)} />
            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 20 }}>
              <button type="button" className="wf-button" style={{ width: 122 }} onClick={() => close(null)}>
                取消
              </button>
              <button type="submit" className="wf-button default" style={{ width: 196 }}>
                確認
              </button>
            </div>
          </form>
        )}
        {spec.kind === 'list' && (
          <div style={{ width: 640, padding: '10px 12px 12px' }}>
            <div className="wf-listbox">
              {spec.items.map((it, i) => (
                <div key={i} className={i === selected ? 'selected' : ''} onClick={() => setSelected(i)} onDoubleClick={() => close(i)}>
                  {it}
                </div>
              ))}
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 24 }}>
              <button className="wf-button" style={{ width: 168 }} onClick={() => close(null)}>
                取消
              </button>
              <button
                ref={defaultRef}
                className="wf-button default"
                style={{ width: 168 }}
                disabled={spec.items.length === 0}
                onClick={() => close(selected)}
              >
                確認
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
