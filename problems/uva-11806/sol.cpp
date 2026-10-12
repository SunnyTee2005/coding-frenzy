#include <cstdio>
const int MOD = 1000007;
int C[405][505];
int main() {
    for (int i = 0; i <= 400; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= 500 && j <= i; ++j) C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
    }
    int t; scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        int m, n, k; scanf("%d %d %d", &m, &n, &k);
        long long ans = 0;
        // 排容：枚舉哪些邊界（上、下、左、右）完全沒人
        for (int mask = 0; mask < 16; ++mask) {
            int r = m, c = n, bits = 0;
            if (mask & 1) { --r; ++bits; }
            if (mask & 2) { --r; ++bits; }
            if (mask & 4) { --c; ++bits; }
            if (mask & 8) { --c; ++bits; }
            if (r < 0 || c < 0 || k > r * c) continue;
            ans += (bits % 2 ? -1 : 1) * C[r * c][k];
        }
        printf("Case %d: %lld\n", cs, ((ans % MOD) + MOD) % MOD);
    }
}
