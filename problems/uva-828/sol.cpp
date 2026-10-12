#include <iostream>
#include <string>
using namespace std;
int main() {
    string line;
    getline(cin, line);
    int t = stoi(line);
    for (int cs = 0; cs < t; ++cs) {
        while (getline(cin, line) && line.find_first_not_of(" \r") == string::npos) {}
        string L = line;
        getline(cin, line); int N = stoi(line);
        getline(cin, line); int q = stoi(line);
        bool inL[26] = {};
        for (char ch : L) inL[ch - 'A'] = true;
        auto deciph = [&](char ch) { return char('A' + (ch - 'A' - N + 26) % 26); };
        if (cs) cout << "\n";
        while (q--) {
            getline(cin, line);
            string out;
            size_t m = 0;  // 目前用到 L 的第 m 個字母（從 0 算）
            bool ok = true;
            for (size_t i = 0; i < line.size() && ok;) {
                char ch = line[i];
                if (ch == ' ') { out += ' '; ++i; continue; }
                if (ch == L[m % L.size()] && i + 2 < line.size() && line[i + 2] == L[(m + 1) % L.size()] && line[i + 1] != ' ' &&
                    inL[deciph(line[i + 1]) - 'A']) {
                    out += deciph(line[i + 1]); ++m; i += 3;
                } else {
                    char p = deciph(ch);
                    if (inL[p - 'A']) ok = false;
                    out += p; ++i;
                }
            }
            cout << (ok ? out : "error in encryption") << "\n";
        }
    }
}
