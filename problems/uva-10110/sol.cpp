#include <cmath>
#include <cstdio>
int main() {
    unsigned long long n;
    while (scanf("%llu", &n) == 1 && n) {
        unsigned long long r = (unsigned long long)sqrtl((long double)n);
        while (r * r > n) --r;
        while ((r + 1) * (r + 1) <= n) ++r;
        puts(r * r == n ? "yes" : "no");
    }
}
