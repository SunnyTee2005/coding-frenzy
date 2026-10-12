#include <cstdio>
#include <cstring>
bool seen[20005];
int main() {
    int n, b[105], cs = 0;
    while (scanf("%d", &n) == 1) {
        for (int i = 0; i < n; ++i) scanf("%d", &b[i]);
        bool ok = b[0] >= 1;
        for (int i = 1; i < n; ++i) if (b[i] <= b[i - 1]) ok = false;
        memset(seen, 0, sizeof seen);
        for (int i = 0; i < n && ok; ++i)
            for (int j = i; j < n && ok; ++j) {
                if (seen[b[i] + b[j]]) ok = false;
                seen[b[i] + b[j]] = true;
            }
        printf("Case #%d: It is %sa B2-Sequence.\n\n", ++cs, ok ? "" : "not ");
    }
}
