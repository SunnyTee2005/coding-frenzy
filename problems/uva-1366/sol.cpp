#include <algorithm>
#include <cstdio>
using namespace std;
int y[505][505], b[505][505];
long long dp[505][505];
int main() {
    int n, m;
    while (scanf("%d %d", &n, &m) == 2 && (n || m)) {
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= m; ++j) { scanf("%d", &y[i][j]); y[i][j] += y[i][j - 1]; }  // 列前綴和
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= m; ++j) { scanf("%d", &b[i][j]); b[i][j] += b[i - 1][j]; }  // 行前綴和
        for (int i = 0; i <= n; ++i) dp[i][0] = 0;
        for (int j = 0; j <= m; ++j) dp[0][j] = 0;
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j)
                dp[i][j] = max(dp[i - 1][j] + y[i][j], dp[i][j - 1] + b[i][j]);
        printf("%lld\n", dp[n][m]);
    }
}
