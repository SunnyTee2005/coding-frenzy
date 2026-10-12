#include <cstdio>
typedef unsigned long long u64;
u64 mod;
void mul(u64 a[2][2], u64 b[2][2]) {
    u64 c[2][2];
    for (int i = 0; i < 2; ++i) for (int j = 0; j < 2; ++j) c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % mod;
    for (int i = 0; i < 2; ++i) for (int j = 0; j < 2; ++j) a[i][j] = c[i][j];
}
int main() {
    long long n; int m;
    while (scanf("%lld %d", &n, &m) == 2) {
        mod = 1ULL << m;
        u64 r[2][2] = {{1 % mod, 0}, {0, 1 % mod}}, b[2][2] = {{1, 1}, {1, 0}};
        for (long long e = n; e; e >>= 1) { if (e & 1) mul(r, b); mul(b, b); }
        printf("%llu\n", r[0][1] % mod);  // [[F(n+1), F(n)], [F(n), F(n-1)]]
    }
}
