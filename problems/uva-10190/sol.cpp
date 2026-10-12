#include <cstdio>
int main() {
    long long n, m;
    while (scanf("%lld %lld", &n, &m) == 2) {
        if (n < 2 || m < 2) { puts("Boring!"); continue; }
        long long x = n;
        while (x > 1 && x % m == 0) x /= m;
        if (x != 1) { puts("Boring!"); continue; }
        for (x = n; x > 1; x /= m) printf("%lld ", x);
        printf("1\n");
    }
}
