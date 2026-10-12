#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n, lo = 100, hi = -1; scanf("%d", &n);
        for (int i = 0; i < n; ++i) { int x; scanf("%d", &x); if (x < lo) lo = x; if (x > hi) hi = x; }
        printf("%d\n", 2 * (hi - lo));
    }
}
