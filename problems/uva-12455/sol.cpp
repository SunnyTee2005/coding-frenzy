#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n, p, b[25]; scanf("%d %d", &n, &p);
        for (int i = 0; i < p; ++i) scanf("%d", &b[i]);
        bool ok = false;
        for (int mask = 0; mask < (1 << p) && !ok; ++mask) {
            int s = 0;
            for (int i = 0; i < p; ++i) if (mask >> i & 1) s += b[i];
            if (s == n) ok = true;
        }
        puts(ok ? "YES" : "NO");
    }
}
