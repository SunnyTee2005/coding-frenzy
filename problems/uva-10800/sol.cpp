#include <iostream>
#include <map>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    for (int c = 1; c <= t; ++c) {
        string s; cin >> s;
        map<int, string> rows;
        int h = 0;
        for (size_t i = 0; i < s.size(); ++i) {
            int level; char ch;
            if (s[i] == 'R') { level = h; ch = '/'; ++h; }
            else if (s[i] == 'F') { --h; level = h; ch = '\\'; }
            else { level = h; ch = '_'; }
            string &r = rows[level];
            if (r.size() < i + 1) r.resize(i + 1, ' ');
            r[i] = ch;
        }
        cout << "Case #" << c << ":\n";
        for (auto it = rows.rbegin(); it != rows.rend(); ++it) cout << "| " << it->second << "\n";
        cout << "+" << string(s.size() + 2, '-') << "\n\n";
    }
}
