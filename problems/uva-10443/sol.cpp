#include <cstdio>
#include <cstring>
char g[105][105], ng[105][105];
int main() {
    int t; scanf("%d", &t);
    const int dr[] = {1, -1, 0, 0}, dc[] = {0, 0, 1, -1};
    for (int cs = 0; cs < t; ++cs) {
        int r, c, n; scanf("%d %d %d", &r, &c, &n);
        for (int i = 0; i < r; ++i) scanf("%s", g[i]);
        while (n--) {
            for (int i = 0; i < r; ++i) {
                for (int j = 0; j < c; ++j) {
                    // 被誰打敗：R 被 P、S 被 R、P 被 S
                    char beater = g[i][j] == 'R' ? 'P' : g[i][j] == 'S' ? 'R' : 'S';
                    ng[i][j] = g[i][j];
                    for (int d = 0; d < 4; ++d) {
                        int a = i + dr[d], b = j + dc[d];
                        if (a >= 0 && b >= 0 && a < r && b < c && g[a][b] == beater) ng[i][j] = beater;
                    }
                }
                ng[i][c] = 0;
            }
            memcpy(g, ng, sizeof g);
        }
        if (cs) printf("\n");
        for (int i = 0; i < r; ++i) printf("%s\n", g[i]);
    }
}
