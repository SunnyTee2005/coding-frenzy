#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        long long n; scanf("%lld", &n);
        long long res = 0;
        // n / i 只有 O(sqrt n) 種不同的值，一段一段加
        for (long long i = 1; i <= n;) {
            long long q = n / i, last = n / q;
            res += q * (last - i + 1);
            i = last + 1;
        }
        printf("%lld\n", res);
    }
}
