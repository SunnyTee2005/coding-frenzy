// 瀏覽器開發用的假後端：固定一題、程式碼含 "WA" 就回 WRONG-ANSWER，其餘一律 CORRECT。
import type { JudgeApi } from './api'
import type { ProblemDetail } from './types'

const sample: ProblemDetail = {
  meta: { id: '10055', title: 'Hashmat the Brave Warrior', stars: 1, time_limit: 3, uva: 10055 },
  statement: '（mock）算出兩數相差的絕對值。',
  samples: [{ input: '10 12\n10 14\n100 200\n', output: '2\n4\n100\n' }],
}

const delay = <T,>(value: T) => new Promise<T>((r) => setTimeout(() => r(value), 150))

export const mockBackend: JudgeApi = {
  toolchainStatus: () =>
    delay({
      commandLineToolsInstalled: true,
      tools: [
        { lang_id: 'c', display: 'C', program: '/usr/bin/clang', version: 'mock' },
        { lang_id: 'cpp', display: 'C++', program: '/usr/bin/clang++', version: 'mock' },
        { lang_id: 'python', display: 'Python 3', program: '/usr/bin/python3', version: 'mock' },
      ],
    }),
  installCommandLineTools: () => delay(undefined),
  languages: () =>
    delay([
      { id: 'c', display: 'C', source: 'main.c' },
      { id: 'cpp', display: 'C++', source: 'main.cpp' },
      { id: 'python', display: 'Python 3', source: 'main.py' },
    ]),
  problems: () => delay([sample.meta]),
  problem: () => delay(sample),
  runTests: (_id, _lang, source) =>
    delay({
      verdict: source.includes('WA') ? 'WRONG-ANSWER' : 'CORRECT',
      compile_message: null,
      cases: [],
    }),
  runCustom: (_id, _lang, _source, input) =>
    delay({ compileMessage: null, status: { Exited: 0 }, stdout: input, stderr: '', timeMs: 1 }),
  formalJudge: (_id, _lang, source) =>
    delay({ verdict: source.includes('WA') ? 'WRONG-ANSWER' : 'CORRECT', compileMessage: null, timeMs: 1 }),
}
