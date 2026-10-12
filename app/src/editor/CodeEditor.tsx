// 仿考場 Alsing SyntaxBox 的程式編輯器：Courier New、行號、折疊符號、
// 關鍵字藍色、字串與運算子紅色、註解綠色。考場編輯器沒有自動完成，這裡也不開。

import { useEffect, useRef } from 'react'
import { EditorState, Compartment } from '@codemirror/state'
import { EditorView, keymap, lineNumbers, highlightActiveLineGutter, drawSelection } from '@codemirror/view'
import { defaultKeymap, history, historyKeymap, indentWithTab } from '@codemirror/commands'
import { foldGutter, syntaxHighlighting, HighlightStyle, indentOnInput, bracketMatching, foldKeymap } from '@codemirror/language'
import { cpp } from '@codemirror/lang-cpp'
import { python } from '@codemirror/lang-python'
import { tags as t } from '@lezer/highlight'

const syntaxBoxStyle = HighlightStyle.define([
  { tag: [t.keyword, t.typeName, t.standard(t.typeName), t.modifier, t.controlKeyword, t.definitionKeyword, t.bool, t.null], color: '#0000ff', fontWeight: 'bold' },
  { tag: [t.string, t.special(t.string), t.character], color: '#ff0000' },
  { tag: [t.operator, t.arithmeticOperator, t.compareOperator, t.bitwiseOperator, t.logicOperator, t.updateOperator], color: '#ff0000' },
  { tag: [t.comment, t.lineComment, t.blockComment], color: '#008000' },
  { tag: [t.processingInstruction, t.meta], color: '#000000' },
  { tag: [t.number], color: '#000000' },
])

const theme = EditorView.theme({
  '&': { height: '100%', backgroundColor: '#fff' },
  '.cm-scroller': { fontFamily: 'var(--code-font)', lineHeight: '1.32' },
  '.cm-content': { caretColor: '#000', padding: '2px 0' },
  '.cm-gutters': { backgroundColor: '#fff', color: '#2b91af', borderRight: '1px solid #ddd' },
  '.cm-lineNumbers .cm-gutterElement': { padding: '0 6px 0 10px', minWidth: '34px' },
  '.cm-foldGutter .cm-gutterElement': { color: '#888', fontSize: '11px', width: '12px' },
  '.cm-activeLineGutter': { backgroundColor: 'transparent' },
  '&.cm-focused': { outline: 'none' },
  '.cm-selectionBackground, &.cm-focused .cm-selectionBackground': { backgroundColor: '#add6ff !important' },
  '.cm-matchingBracket': { backgroundColor: '#dbe9ff', outline: '1px solid #9ab' },
})

export interface CodeEditorProps {
  value: string
  onChange: (v: string) => void
  lang: string
  fontSize: number
  readOnly?: boolean
}

export function CodeEditor({ value, onChange, lang, fontSize, readOnly }: CodeEditorProps) {
  const host = useRef<HTMLDivElement>(null)
  const view = useRef<EditorView | null>(null)
  const langConf = useRef(new Compartment())
  const fontConf = useRef(new Compartment())
  const roConf = useRef(new Compartment())
  const onChangeRef = useRef(onChange)
  onChangeRef.current = onChange

  useEffect(() => {
    const v = new EditorView({
      parent: host.current!,
      state: EditorState.create({
        doc: value,
        extensions: [
          lineNumbers(),
          foldGutter({ openText: '⊟', closedText: '⊞' }),
          highlightActiveLineGutter(),
          drawSelection(),
          history(),
          indentOnInput(),
          bracketMatching(),
          EditorState.tabSize.of(4),
          keymap.of([...defaultKeymap, ...historyKeymap, ...foldKeymap, indentWithTab]),
          syntaxHighlighting(syntaxBoxStyle),
          theme,
          langConf.current.of(lang === 'python' ? python() : cpp()),
          fontConf.current.of(EditorView.theme({ '.cm-scroller': { fontSize: `${fontSize}px` } })),
          roConf.current.of(EditorState.readOnly.of(!!readOnly)),
          EditorView.updateListener.of((u) => {
            if (u.docChanged) onChangeRef.current(u.state.doc.toString())
          }),
        ],
      }),
    })
    view.current = v
    return () => v.destroy()
    // 只在掛載時建立；之後的變更由下面的 effect 處理
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  // 外部換掉內容（提檔續答、貼上範例）時同步
  useEffect(() => {
    const v = view.current
    if (v && v.state.doc.toString() !== value) v.dispatch({ changes: { from: 0, to: v.state.doc.length, insert: value } })
  }, [value])

  useEffect(() => {
    view.current?.dispatch({ effects: langConf.current.reconfigure(lang === 'python' ? python() : cpp()) })
  }, [lang])

  useEffect(() => {
    view.current?.dispatch({ effects: fontConf.current.reconfigure(EditorView.theme({ '.cm-scroller': { fontSize: `${fontSize}px` } })) })
  }, [fontSize])

  useEffect(() => {
    view.current?.dispatch({ effects: roConf.current.reconfigure(EditorState.readOnly.of(!!readOnly)) })
  }, [readOnly])

  return <div ref={host} style={{ height: '100%' }} />
}
