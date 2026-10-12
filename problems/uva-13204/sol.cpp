#include <cstdio>
const long long MOD = 1000000007;
long long fact[500005];
int main() {
    fact[0] = 1;
    for (int i = 1; i <= 500000; ++i) fact[i] = fact[i - 1] * i % MOD;
    long long n;
    while (scanf("%lld", &n) == 1) {
        long long k = n / 2, ans = fact[k] * fact[k] % MOD;
        if (n % 2) ans = ans * (n % MOD) % MOD;
        printf("%lld\n", ans);
    }
}
