#include <cstdio>
#include <cstring>
// can[c][s]：選 c 個數、總和為 s（位移 2500）是否做得到
bool can[52][5005];
int main() {
    int n, m;
    while (scanf("%d %d", &n, &m) == 2) {
        int a[105], total = 0;
        for (int i = 0; i < n + m; ++i) { scanf("%d", &a[i]); total += a[i]; }
        int sm = n < m ? n : m;
        memset(can, 0, sizeof can);
        can[0][2500] = true;
        for (int i = 0; i < n + m; ++i)
            for (int c = sm; c >= 1; --c)
                for (int s = 0; s <= 5000; ++s)
                    if (can[c - 1][s] && s + a[i] >= 0 && s + a[i] <= 5000) can[c][s + a[i]] = true;
        long long best = -1000000000, worst = 1000000000;
        for (int s = 0; s <= 5000; ++s)
            if (can[sm][s]) {
                long long x = s - 2500, v = x * (total - x);
                if (v > best) best = v;
                if (v < worst) worst = v;
            }
        printf("%lld %lld\n", best, worst);
    }
}
