#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>
using namespace std;
int main() {
    int n, d, cs = 0;
    while (scanf("%d %d", &n, &d) == 2 && (n || d)) {
        vector<pair<double, double>> iv;  // (右端, 左端)
        bool bad = d < 0;
        for (int i = 0; i < n; ++i) {
            int x, y; scanf("%d %d", &x, &y);
            if (y > d || y < -d) { bad = true; continue; }
            double w = sqrt((double)d * d - (double)y * y);
            iv.push_back({x + w, x - w});
        }
        int ans = -1;
        if (!bad) {
            sort(iv.begin(), iv.end());
            ans = 0;
            double last = -1e18;
            for (auto& p : iv) if (p.second > last) { ++ans; last = p.first; }
        }
        printf("Case %d: %d\n", ++cs, ans);
    }
}
