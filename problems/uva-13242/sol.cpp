#include <cstdio>
#include <cstdlib>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        long long cap, target; int n;
        scanf("%lld %lld %d", &cap, &target, &n);
        static long long v[3005], tp[3005];
        for (int i = 0; i < n; ++i) scanf("%lld %lld", &v[i], &tp[i]);
        int bi = -1, bj = -1;
        long long bnum = 0, bden = 1;  // 最佳溫差 = bnum / bden
        for (int i = 0; i < n; ++i) {
            long long vol = 0, heat = 0;
            for (int j = i; j < n; ++j) {
                vol += v[j]; heat += v[j] * tp[j];
                if (vol > cap) break;
                if (2 * vol < cap) continue;
                long long num = llabs(heat - target * vol);  // 溫差 = num / vol
                if (num > 5 * vol) continue;
                if (bi < 0 || num * bden < bnum * vol) { bi = i; bj = j; bnum = num; bden = vol; }
            }
        }
        if (bi < 0) puts("Not possible");
        else printf("%d %d\n", bi, bj);
    }
}
