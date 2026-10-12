#include <cstdio>
int main() {
    int k;
    while (scanf("%d", &k) == 1 && k) {
        int n, m; scanf("%d %d", &n, &m);
        while (k--) {
            int x, y; scanf("%d %d", &x, &y);
            if (x == n || y == m) puts("divisa");
            else if (y > m) puts(x < n ? "NO" : "NE");
            else puts(x < n ? "SO" : "SE");
        }
    }
}
