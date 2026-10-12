#include <cstdio>
int main() {
    static int dp[101][101];
    for (int n = 0; n <= 100; ++n) dp[1][n] = 1;
    for (int k = 2; k <= 100; ++k)
        for (int n = 0; n <= 100; ++n) {
            int s = 0;
            for (int x = 0; x <= n; ++x) s = (s + dp[k - 1][n - x]) % 1000000;
            dp[k][n] = s;
        }
    int n, k;
    while (scanf("%d %d", &n, &k) == 2 && (n || k)) printf("%d\n", dp[k][n]);
}
