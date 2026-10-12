// DockPanel Suite 樣式的面板與可拖曳分隔線。

import { useRef, type ReactNode } from 'react'

export function DockPane({
  title,
  children,
  onClose,
  footer,
  style,
}: {
  title: string
  children: ReactNode
  onClose?: () => void
  footer?: ReactNode
  style?: React.CSSProperties
}) {
  return (
    <div className="wf-dock-pane" style={style}>
      <div className="wf-dock-caption">
        <span className="wf-dock-title">{title}</span>
        <button aria-label="自動隱藏" tabIndex={-1}>
          ⊣
        </button>
        {onClose && (
          <button aria-label="關閉" tabIndex={-1} onClick={onClose}>
            ✕
          </button>
        )}
      </div>
      <div className="wf-dock-body">{children}</div>
      {footer}
    </div>
  )
}

/** 拖曳改變相鄰面板尺寸。`onDrag` 收到的是滑鼠位移（px）。 */
export function Splitter({ direction, onDrag }: { direction: 'v' | 'h'; onDrag: (delta: number) => void }) {
  const last = useRef(0)
  return (
    <div
      className={direction === 'v' ? 'wf-splitter-v' : 'wf-splitter-h'}
      onMouseDown={(e) => {
        e.preventDefault()
        last.current = direction === 'v' ? e.clientX : e.clientY
        const move = (ev: MouseEvent) => {
          const pos = direction === 'v' ? ev.clientX : ev.clientY
          onDrag(pos - last.current)
          last.current = pos
        }
        const up = () => {
          window.removeEventListener('mousemove', move)
          window.removeEventListener('mouseup', up)
        }
        window.addEventListener('mousemove', move)
        window.addEventListener('mouseup', up)
      }}
    />
  )
}
