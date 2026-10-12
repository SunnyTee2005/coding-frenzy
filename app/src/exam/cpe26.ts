// CPE26 選集（2027 年起每次 CPE 會有一題從此選出）。來源：https://cpe.mcu.edu.tw/cpelist.php
// [CPE26 編號, UVa 編號, 題名, 分類]

export interface Cpe26Entry {
  cpe: number
  uva: number
  title: string
  category: string
}

const RAW: [number, number, string, string][] = [
  [26011, 272, 'TEX Quotes', '輸入格式'],
  [26012, 11356, 'Dates', '輸入格式'],
  [26013, 1586, 'Molar mass', '輸入格式'],
  [26014, 392, 'Polynomial Showdown', '輸入格式'],
  [26021, 12289, 'One-Two-Three', '字串字元'],
  [26022, 11541, 'Decoding', '字串字元'],
  [26023, 11576, 'Scrolling Sign', '字串字元'],
  [26024, 10921, 'Find The Telephone', '字串字元'],
  [26031, 11650, 'Mirror Clock', '日期時間'],
  [26032, 11947, 'Cancer or Scorpio', '日期時間'],
  [26033, 11219, 'How old are you?', '日期時間'],
  [26034, 11309, 'Counting Chaos', '日期時間'],
  [26041, 12468, 'Zapping', '算子運算'],
  [26042, 10035, 'Primary Arithmetic', '算子運算'],
  [26043, 13178, 'Is it multiple of 3?', '算子運算'],
  [26044, 275, 'Expanding Fractions', '算子運算'],
  [26051, 10699, 'Count the factors', '質因倍數'],
  [26052, 412, 'Pi', '質因倍數'],
  [26053, 993, 'Product of digits', '質因倍數'],
  [26054, 516, 'Prime Land', '質因倍數'],
  [26061, 446, 'Kibbles "n" Bits "n" Bits "n" Bits', '進制基底'],
  [26062, 11398, 'The Base-1 Number System', '進制基底'],
  [26063, 11121, 'Base -2', '進制基底'],
  [26064, 948, 'Fibonaccimal Base', '進制基底'],
  [26071, 10189, 'Minesweeper', '二維寫真'],
  [26072, 10010, "Where's Waldorf?", '二維寫真'],
  [26073, 706, 'LC-Display', '二維寫真'],
  [26074, 10800, 'Not That Kind of Graph', '二維寫真'],
  [26081, 10018, 'Reverse and Add', '規則模擬'],
  [26082, 10409, 'Die Game', '規則模擬'],
  [26083, 11743, 'Credit Check', '規則模擬'],
  [26084, 10258, 'Contest Scoreboard', '規則模擬'],
  [26091, 478, 'Points in Figures: Rectangles, Circles, and Triangles', '正暴窮舉'],
  [26092, 10365, 'Blocks', '正暴窮舉'],
  [26093, 1225, 'Digit Counting', '正暴窮舉'],
  [26094, 11728, 'Alternate Task', '正暴窮舉'],
  [26101, 880, 'Cantor Fractions', '二維排數'],
  [26102, 913, 'Joana and the Odd Numbers', '二維排數'],
  [26103, 10161, 'Ant on a Chessboard', '二維排數'],
  [26104, 10920, 'Spiral Tap', '二維排數'],
  [26111, 530, 'Binomial Showdown', '排列組合'],
  [26112, 10943, 'How do you add?', '排列組合'],
  [26113, 729, 'The Hamming Distance Problem', '排列組合'],
  [26114, 10098, 'Generating Fast', '排列組合'],
  [26121, 10327, 'Flip Sort', '排序處秩'],
  [26122, 11369, 'Shopaholic', '排序處秩'],
  [26123, 11942, 'Lumberjack Sequencing', '排序處秩'],
  [26124, 11039, 'Building designing', '排序處秩'],
  [26131, 642, 'Word Amalgamation', '集合映對'],
  [26132, 12820, 'Cool Word', '集合映對'],
  [26133, 496, 'Simply Subsets', '集合映對'],
  [26134, 10730, 'Antiarithmetic?', '集合映對'],
  [26141, 10935, 'Throwing cards away I', '堆疊佇列'],
  [26142, 13190, 'Rockabye Tobby', '堆疊佇列'],
  [26143, 673, 'Parentheses Balance', '堆疊佇列'],
  [26144, 11352, 'Crazy King', '堆疊佇列'],
]

export const CPE26: Cpe26Entry[] = RAW.map(([cpe, uva, title, category]) => ({ cpe, uva, title, category }))
