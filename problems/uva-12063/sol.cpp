#include <cstdio>
#include <cstring>
long long dp[66][66][101];  // dp[位數][1 的個數][餘數]
int main() {
    int t; scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        int n, k; scanf("%d %d", &n, &k);
        long long ans = 0;
        if (n % 2 == 0 && k > 0) {
            memset(dp, 0, sizeof dp);
            dp[1][1][1 % k] = 1;  // 最高位一定是 1
            for (int i = 1; i < n; ++i)
                for (int o = 0; o <= i; ++o)
                    for (int r = 0; r < k; ++r) {
                        long long v = dp[i][o][r];
                        if (!v) continue;
                        dp[i + 1][o][(r * 2) % k] += v;
                        dp[i + 1][o + 1][(r * 2 + 1) % k] += v;
                    }
            ans = dp[n][n / 2][0];
        }
        printf("Case %d: %lld\n", cs, ans);
    }
}
