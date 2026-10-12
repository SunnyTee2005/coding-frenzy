#include <algorithm>
#include <cstdio>
#include <map>
#include <vector>
using namespace std;
int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        vector<long long> a(n);
        for (auto& x : a) scanf("%lld", &x);
        sort(a.begin(), a.end());
        // a + b = d - c：先存所有 a+b，再枚舉 d、c
        multimap<long long, pair<int, int>> sums;
        for (int i = 0; i < n; ++i) for (int j = i + 1; j < n; ++j) sums.insert({a[i] + a[j], {i, j}});
        bool found = false;
        for (int d = n - 1; d >= 0 && !found; --d)
            for (int c = 0; c < n && !found; ++c) {
                if (c == d) continue;
                auto range = sums.equal_range(a[d] - a[c]);
                for (auto it = range.first; it != range.second; ++it) {
                    int i = it->second.first, j = it->second.second;
                    if (i != c && i != d && j != c && j != d) { found = true; printf("%lld\n", a[d]); break; }
                }
            }
        if (!found) puts("no solution");
    }
}
