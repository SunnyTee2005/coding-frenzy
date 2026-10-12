#include <cctype>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    int t; cin >> t;
    for (int c = 0; c < t; ++c) {
        int m, n; cin >> m >> n;
        vector<string> g(m);
        for (auto &r : g) { cin >> r; for (auto &ch : r) ch = tolower(ch); }
        int k; cin >> k;
        if (c) cout << "\n";
        while (k--) {
            string w; cin >> w;
            for (auto &ch : w) ch = tolower(ch);
            bool found = false;
            for (int i = 0; i < m && !found; ++i)
                for (int j = 0; j < n && !found; ++j)
                    for (int di = -1; di <= 1 && !found; ++di)
                        for (int dj = -1; dj <= 1 && !found; ++dj) {
                            if (!di && !dj) continue;
                            size_t p = 0;
                            int x = i, y = j;
                            while (p < w.size() && x >= 0 && x < m && y >= 0 && y < n && g[x][y] == w[p]) { ++p; x += di; y += dj; }
                            if (p == w.size()) { cout << i + 1 << " " << j + 1 << "\n"; found = true; }
                        }
        }
    }
}
