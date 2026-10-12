#include <cstdio>
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        long long g = 0;
        for (int i = 1; i < n; ++i) for (int j = i + 1; j <= n; ++j) g += gcd(i, j);
        printf("%lld\n", g);
    }
}
