#include <iostream>
#include <string>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int k, w; cin >> k >> w;
        string prev, cur; cin >> prev;
        long long len = k;
        for (int i = 1; i < w; ++i) {
            cin >> cur;
            int best = 0;
            for (int m = k; m >= 0; --m)
                if (prev.compare(k - m, m, cur, 0, m) == 0) { best = m; break; }
            len += k - best;
            prev = cur;
        }
        cout << len << "\n";
    }
}
