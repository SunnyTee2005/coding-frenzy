#include <cstdio>
int main() {
    long long n, k;
    while (scanf("%lld %lld", &n, &k) == 2 && (n || k)) {
        if (k > n - k) k = n - k;
        long long r = 1;
        for (long long i = 1; i <= k; ++i) r = r * (n - k + i) / i;
        printf("%lld\n", r);
    }
}
