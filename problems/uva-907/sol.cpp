#include <cstdio>
int d[605];
int main() {
    int n, k;
    while (scanf("%d %d", &n, &k) == 2) {
        int lo = 0, hi = 0;
        for (int i = 0; i <= n; ++i) { scanf("%d", &d[i]); if (d[i] > lo) lo = d[i]; hi += d[i]; }
        // 二分搜尋每天最多走多少，貪心算需要幾天
        while (lo < hi) {
            int mid = (lo + hi) / 2, days = 1, cur = 0;
            for (int i = 0; i <= n; ++i) {
                if (cur + d[i] > mid) { ++days; cur = 0; }
                cur += d[i];
            }
            if (days <= k + 1) hi = mid; else lo = mid + 1;
        }
        printf("%d\n", lo);
    }
}
