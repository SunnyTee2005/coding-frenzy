#include <algorithm>
#include <cstdio>
int len(long long n) { int c = 1; while (n != 1) { n = n % 2 ? 3 * n + 1 : n / 2; ++c; } return c; }
int main() {
    int i, j;
    while (scanf("%d %d", &i, &j) == 2) {
        int lo = std::min(i, j), hi = std::max(i, j), best = 0;
        for (int n = lo; n <= hi; ++n) best = std::max(best, len(n));
        printf("%d %d %d\n", i, j, best);
    }
}
