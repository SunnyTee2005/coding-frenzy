#include <cstdio>
const long long MOD = 1000000007;
long long C[1005][1005], fact[1005];
int main() {
    for (int i = 0; i <= 1000; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
    }
    fact[0] = 1;
    for (int i = 1; i <= 1000; ++i) fact[i] = fact[i - 1] * i % MOD;
    int t; scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        int n, m, k; scanf("%d %d %d", &n, &m, &k);
        // 先選 k 個固定點，剩下前 m-k 個位置用排容原理排除固定點
        long long s = 0;
        for (int i = 0; i <= m - k; ++i) {
            long long term = C[m - k][i] * fact[n - k - i] % MOD;
            s = (s + (i % 2 ? MOD - term : term)) % MOD;
        }
        printf("Case %d: %lld\n", cs, C[m][k] * s % MOD);
    }
}
