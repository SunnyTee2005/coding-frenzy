#include <cstdio>
int main() {
    long long a, b, c, d, l;
    while (scanf("%lld %lld %lld %lld %lld", &a, &b, &c, &d, &l) == 5 && (a || b || c || d || l)) {
        int cnt = 0;
        for (long long x = 0; x <= l; ++x) if ((a * x * x + b * x + c) % d == 0) ++cnt;
        printf("%d\n", cnt);
    }
}
