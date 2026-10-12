#include <cmath>
#include <cstdio>
int main() {
    long long n;
    while (scanf("%lld", &n) == 1 && n) {
        long long k = (long long)ceil(sqrt((double)n));
        while (k * k < n) ++k;
        while ((k - 1) * (k - 1) >= n) --k;
        long long d = k * k - n;  // 從這一層最後一格往回數
        long long x, y;
        if (d < k) { x = d + 1; y = k; } else { x = k; y = 2 * k - 1 - d; }
        if (k % 2 == 0) { long long t = x; x = y; y = t; }
        printf("%lld %lld\n", x, y);
    }
}
