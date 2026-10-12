#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    for (int c = 1; c <= t; ++c) {
        int n, prev, hi = 0, lo = 0; scanf("%d %d", &n, &prev);
        for (int i = 1; i < n; ++i) {
            int x; scanf("%d", &x);
            if (x > prev) ++hi; else if (x < prev) ++lo;
            prev = x;
        }
        printf("Case %d: %d %d\n", c, hi, lo);
    }
}
