#include <cstdio>
int main() {
    int c; scanf("%d", &c);
    while (c--) {
        int n; scanf("%d", &n);
        int best = 1 << 30;
        for (int a = 1; a <= n; ++a) if (n % a == 0)
            for (int b = 1; b <= n / a; ++b) if ((n / a) % b == 0) {
                int h = n / a / b;
                int s = 2 * (a * b + b * h + a * h);
                if (s < best) best = s;
            }
        printf("%d\n", best);
    }
}
