#include <cstdio>
int main() {
    int primes[30], np = 0;
    for (int i = 2; i <= 100; ++i) {
        bool p = true;
        for (int d = 2; d * d <= i; ++d) if (i % d == 0) p = false;
        if (p) primes[np++] = i;
    }
    int n;
    while (scanf("%d", &n) == 1 && n) {
        printf("%3d! =", n);
        for (int i = 0, shown = 0; i < np && primes[i] <= n; ++i, ++shown) {
            int c = 0;
            for (int x = n / primes[i]; x; x /= primes[i]) c += x;
            if (shown && shown % 15 == 0) printf("\n      ");
            printf("%3d", c);
        }
        printf("\n");
    }
}
