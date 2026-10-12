// 自繪的 Windows 7 樣式視窗外框（標題列 + 最小化 / 最大化 / 關閉）。
// Tauri 視窗設定為無邊框，拖曳標題列靠 data-tauri-drag-region。

import type { ReactNode } from 'react'
import { getCurrentWindow } from '@tauri-apps/api/window'
import { isTauri } from '../judge/api'

function AppIcon() {
  return (
    <svg className="wf-app-icon" viewBox="0 0 16 16" aria-hidden>
      <rect x="1" y="1" width="6" height="6" fill="#e2412c" />
      <rect x="9" y="1" width="6" height="6" fill="#f0a20b" />
      <rect x="1" y="9" width="6" height="6" fill="#2f7fd8" />
      <rect x="9" y="9" width="6" height="6" fill="#3ea53a" />
    </svg>
  )
}

const win = () => (isTauri ? getCurrentWindow() : null)

/**
 * `inDialog`：對話框內的標題列。最小化 / 最大化只是外觀（考場的對話框也有），不會動到整個視窗；
 * `closeOnly`：訊息框只有關閉鈕。
 */
export function TitleBar({ title, onClose, closeOnly, inDialog }: { title: string; onClose?: () => void; closeOnly?: boolean; inDialog?: boolean }) {
  const real = !inDialog
  return (
    <div className="wf-titlebar" data-tauri-drag-region={real ? true : undefined} onDoubleClick={() => real && win()?.toggleMaximize()}>
      <AppIcon />
      <div className="wf-title">{title}</div>
      <div className="wf-caption-buttons">
        {!closeOnly && (
          <>
            <button aria-label="最小化" onClick={() => real && win()?.minimize()}>
              ▁
            </button>
            <button aria-label="最大化" onClick={() => real && win()?.toggleMaximize()}>
              ❐
            </button>
          </>
        )}
        <button className="wf-close" aria-label="關閉" onClick={onClose ?? (() => win()?.close())}>
          ✕
        </button>
      </div>
    </div>
  )
}

export function Window({ title, children, onClose }: { title: string; children: ReactNode; onClose?: () => void }) {
  return (
    <div className="wf-window">
      <TitleBar title={title} onClose={onClose} />
      <div className="wf-body">{children}</div>
    </div>
  )
}

export function closeCurrentWindow() {
  if (isTauri) getCurrentWindow().close()
  else window.close()
}
