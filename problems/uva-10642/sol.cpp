#include <cstdio>
long long idx(long long x, long long y) { long long d = x + y; return d * (d + 1) / 2 + x; }
int main() {
    int n; scanf("%d", &n);
    for (int c = 1; c <= n; ++c) {
        long long a, b, x, y; scanf("%lld %lld %lld %lld", &a, &b, &x, &y);
        printf("Case %d: %lld\n", c, idx(x, y) - idx(a, b));
    }
}
