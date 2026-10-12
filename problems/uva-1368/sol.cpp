#include <iostream>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    const string N = "ACGT";
    while (t--) {
        int m, n; cin >> m >> n;
        string s[55];
        for (int i = 0; i < m; ++i) cin >> s[i];
        string best;
        int err = 0;
        for (int j = 0; j < n; ++j) {
            int cnt[4] = {};
            for (int i = 0; i < m; ++i) ++cnt[N.find(s[i][j])];
            int b = 0;
            for (int c = 1; c < 4; ++c) if (cnt[c] > cnt[b]) b = c;
            best += N[b];
            err += m - cnt[b];
        }
        cout << best << "\n" << err << "\n";
    }
}
