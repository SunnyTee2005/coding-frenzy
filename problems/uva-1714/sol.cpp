#include <array>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
char g[55][55], text[10010];
int nxt[55][55][4][2];
int best[55][55];       // 抵達這格時已經打好的最多字數
int main() {
    int r, c;
    const int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    while (scanf("%d %d", &r, &c) == 2) {
        for (int i = 0; i < r; ++i) scanf("%s", g[i]);
        scanf("%s", text);
        int len = strlen(text);
        text[len++] = '*';
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                for (int d = 0; d < 4; ++d) {
                    int ni = i, nj = j;
                    while (ni >= 0 && nj >= 0 && ni < r && nj < c && g[ni][nj] == g[i][j]) { ni += dr[d]; nj += dc[d]; }
                    if (ni < 0 || nj < 0 || ni >= r || nj >= c) { ni = i; nj = j; }
                    nxt[i][j][d][0] = ni; nxt[i][j][d][1] = nj;
                }
        memset(best, -1, sizeof best);
        // BFS 狀態 (格子, 已打字數)；同一格只保留打得最多的狀態（打得多一定不會比較差）
        queue<array<int, 4>> q;
        q.push({0, 0, 0, 0});
        best[0][0] = 0;
        int ans = -1;
        while (!q.empty()) {
            auto s = q.front(); q.pop();
            int i = s[0], j = s[1], typed = s[2], d = s[3];
            if (g[i][j] == text[typed]) {
                if (typed + 1 == len) { ans = d + 1; break; }
                if (best[i][j] < typed + 1) { best[i][j] = typed + 1; q.push({i, j, typed + 1, d + 1}); }
                continue;
            }
            for (int k = 0; k < 4; ++k) {
                int ni = nxt[i][j][k][0], nj = nxt[i][j][k][1];
                if (best[ni][nj] < typed) { best[ni][nj] = typed; q.push({ni, nj, typed, d + 1}); }
            }
        }
        printf("%d\n", ans);
    }
}
