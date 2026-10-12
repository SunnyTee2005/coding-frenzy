#include <cmath>
#include <cstdio>
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        int a[64];
        for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
        int pairs = 0, coprime = 0;
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j) {
                ++pairs;
                if (gcd(a[i], a[j]) == 1) ++coprime;
            }
        if (coprime == 0) puts("No estimate for this data set.");
        else printf("%.6f\n", sqrt(6.0 * pairs / coprime));
    }
}
