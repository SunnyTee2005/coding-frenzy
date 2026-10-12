#include <cstdio>
int main() {
    int j, r;
    while (scanf("%d %d", &j, &r) == 2 && (j || r)) {
        int pts[505] = {};
        for (int t = 0; t < j * r; ++t) { int v; scanf("%d", &v); pts[t % j] += v; }
        int best = 0;
        for (int i = 1; i < j; ++i) if (pts[i] >= pts[best]) best = i;
        printf("%d\n", best + 1);
    }
}
