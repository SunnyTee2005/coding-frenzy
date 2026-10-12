#include <cstdio>
long long gcd(long long a, long long b) { return b ? gcd(b, a % b) : a; }
int main() {
    long long v1, d1, v2, d2;
    int cs = 0;
    while (scanf("%lld %lld %lld %lld", &v1, &d1, &v2, &d2) == 4 && (v1 || d1 || v2 || d2)) {
        printf("Case #%d: %s\n", ++cs, d1 * v2 < d2 * v1 ? "You owe me a beer!" : "No beer for the captain.");
        long long num = d1 * v2 + d2 * v1, den = 2 * v1 * v2;
        long long g = gcd(num, den);
        num /= g; den /= g;
        if (den == 1) printf("Avg. arrival time: %lld\n", num);
        else printf("Avg. arrival time: %lld/%lld\n", num, den);
    }
}
