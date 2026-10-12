#include <cstdio>
long long a[105][105];
int main() {
    int t; scanf("%d", &t);
    for (int c = 1; c <= t; ++c) {
        int n; scanf(" N = %d", &n);
        bool ok = true;
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) { scanf("%lld", &a[i][j]); if (a[i][j] < 0) ok = false; }
        for (int i = 0; i < n && ok; ++i)
            for (int j = 0; j < n; ++j) if (a[i][j] != a[n - 1 - i][n - 1 - j]) { ok = false; break; }
        printf("Test #%d: %s\n", c, ok ? "Symmetric." : "Non-symmetric.");
    }
}
