#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
int main() {
    int p; scanf("%d", &p);
    while (p--) {
        int n; scanf("%d", &n);
        std::vector<int> v(n);
        for (int &x : v) scanf("%d", &x);
        std::sort(v.begin(), v.end(), [](int a, int b) { return abs(a) < abs(b); });
        int best = 0;
        for (int start = 0; start < 2; ++start) {
            int cnt = 0, want = start;  // 0 = 要藍（正）、1 = 要紅（負）
            for (int x : v) if ((x > 0) == (want == 0)) { ++cnt; want ^= 1; }
            if (cnt > best) best = cnt;
        }
        printf("%d\n", best);
    }
}
