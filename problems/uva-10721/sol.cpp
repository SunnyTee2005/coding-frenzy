#include <cstdio>
#include <cstring>
long long dp[55][55];  // dp[k][n]：k 條、共 n 單位
int main() {
    int n, k, m;
    while (scanf("%d %d %d", &n, &k, &m) == 3) {
        memset(dp, 0, sizeof dp);
        dp[0][0] = 1;
        for (int b = 1; b <= k; ++b)
            for (int u = 1; u <= n; ++u)
                for (int w = 1; w <= m && w <= u; ++w) dp[b][u] += dp[b - 1][u - w];
        printf("%lld\n", dp[k][n]);
    }
}
