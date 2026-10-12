#include <cstdio>
int main() {
    long long s;
    while (scanf("%lld", &s) == 1 && s) {
        long long n = 1;
        while (n * (n + 1) / 2 <= s) ++n;
        printf("%lld %lld\n", n * (n + 1) / 2 - s, n);
    }
}
