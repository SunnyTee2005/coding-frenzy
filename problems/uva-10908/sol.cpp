#include <cstdio>
char g[105][105];
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int m, n, q; scanf("%d %d %d", &m, &n, &q);
        for (int i = 0; i < m; ++i) scanf("%s", g[i]);
        printf("%d %d %d\n", m, n, q);
        while (q--) {
            int r, c; scanf("%d %d", &r, &c);
            int k = 0;
            for (;;) {
                int nk = k + 1;
                if (r - nk < 0 || c - nk < 0 || r + nk >= m || c + nk >= n) break;
                bool ok = true;
                for (int i = r - nk; i <= r + nk && ok; ++i)
                    for (int j = c - nk; j <= c + nk; ++j)
                        if (g[i][j] != g[r][c]) { ok = false; break; }
                if (!ok) break;
                k = nk;
            }
            printf("%d\n", 2 * k + 1);
        }
    }
}
