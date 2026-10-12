#include <cstdio>

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        int n, cnt[10] = {0};
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
            for (int x = i; x; x /= 10) ++cnt[x % 10];
        for (int d = 0; d < 10; ++d) printf(d ? " %d" : "%d", cnt[d]);
        printf("\n");
    }
    return 0;
}
