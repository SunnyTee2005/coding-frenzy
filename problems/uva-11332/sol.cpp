#include <cstdio>
int main() {
    long long n;
    while (scanf("%lld", &n) == 1 && n) {
        while (n >= 10) {
            long long s = 0;
            for (long long x = n; x; x /= 10) s += x % 10;
            n = s;
        }
        printf("%lld\n", n);
    }
}
