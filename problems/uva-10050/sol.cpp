#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n, p, h[105]; scanf("%d %d", &n, &p);
        for (int i = 0; i < p; ++i) scanf("%d", &h[i]);
        int lost = 0;
        for (int d = 1; d <= n; ++d) {
            if (d % 7 == 6 || d % 7 == 0) continue;
            for (int i = 0; i < p; ++i) if (d % h[i] == 0) { ++lost; break; }
        }
        printf("%d\n", lost);
    }
}
