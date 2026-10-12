#include <algorithm>
#include <cstdio>
using namespace std;
int main() {
    int n, game = 0;
    while (scanf("%d", &n) == 1 && n) {
        int code[1005], g[1005];
        for (int i = 0; i < n; ++i) scanf("%d", &code[i]);
        printf("Game %d:\n", ++game);
        for (;;) {
            bool zero = true;
            for (int i = 0; i < n; ++i) { scanf("%d", &g[i]); if (g[i]) zero = false; }
            if (zero) break;
            int strong = 0, cc[10] = {}, cg[10] = {};
            for (int i = 0; i < n; ++i) {
                if (code[i] == g[i]) ++strong;
                ++cc[code[i]]; ++cg[g[i]];
            }
            int total = 0;
            for (int d = 1; d <= 9; ++d) total += min(cc[d], cg[d]);
            printf("    (%d,%d)\n", strong, total - strong);
        }
    }
}
