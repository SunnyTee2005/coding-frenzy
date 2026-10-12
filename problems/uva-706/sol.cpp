#include <iostream>
#include <string>
using namespace std;
// 七段：a 上、b 右上、c 右下、d 下、e 左下、f 左上、g 中
const char *SEG[10] = {"abcdef", "bc", "abged", "abgcd", "fgbc", "afgcd", "afgecd", "abc", "abcdefg", "abcdfg"};
bool has(int d, char s) { return string(SEG[d]).find(s) != string::npos; }
int main() {
    int s; string n;
    while (cin >> s >> n && !(s == 0 && n == "0")) {
        for (int row = 0; row < 2 * s + 3; ++row) {
            string line;
            for (size_t i = 0; i < n.size(); ++i) {
                int d = n[i] - '0';
                if (i) line += ' ';
                if (row == 0 || row == s + 1 || row == 2 * s + 2) {
                    char seg = row == 0 ? 'a' : row == s + 1 ? 'g' : 'd';
                    line += ' ' + string(s, has(d, seg) ? '-' : ' ') + ' ';
                } else {
                    bool upper = row <= s;
                    line += has(d, upper ? 'f' : 'e') ? '|' : ' ';
                    line += string(s, ' ');
                    line += has(d, upper ? 'b' : 'c') ? '|' : ' ';
                }
            }
            cout << line << "\n";
        }
        cout << "\n";
    }
}
