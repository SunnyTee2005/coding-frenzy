#include <cstdio>
#include <queue>
#include <utility>
using namespace std;
char g[1005][1005];
int fire[1005][1005], joe[1005][1005];
int main() {
    int t; scanf("%d", &t);
    const int dr[] = {1, -1, 0, 0}, dc[] = {0, 0, 1, -1};
    while (t--) {
        int r, c; scanf("%d %d", &r, &c);
        for (int i = 0; i < r; ++i) scanf("%s", g[i]);
        queue<pair<int, int>> q;
        for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j) {
            fire[i][j] = -1; joe[i][j] = -1;
            if (g[i][j] == 'F') { fire[i][j] = 0; q.push({i, j}); }
        }
        while (!q.empty()) {
            auto p = q.front(); q.pop();
            for (int d = 0; d < 4; ++d) {
                int ni = p.first + dr[d], nj = p.second + dc[d];
                if (ni < 0 || nj < 0 || ni >= r || nj >= c || g[ni][nj] == '#' || fire[ni][nj] >= 0) continue;
                fire[ni][nj] = fire[p.first][p.second] + 1; q.push({ni, nj});
            }
        }
        for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j) if (g[i][j] == 'J') { joe[i][j] = 0; q.push({i, j}); }
        int ans = -1;
        while (!q.empty() && ans < 0) {
            auto p = q.front(); q.pop();
            int i = p.first, j = p.second;
            if (i == 0 || j == 0 || i == r - 1 || j == c - 1) { ans = joe[i][j] + 1; break; }
            for (int d = 0; d < 4; ++d) {
                int ni = i + dr[d], nj = j + dc[d], nt = joe[i][j] + 1;
                if (g[ni][nj] == '#' || joe[ni][nj] >= 0) continue;
                if (fire[ni][nj] >= 0 && fire[ni][nj] <= nt) continue;
                joe[ni][nj] = nt; q.push({ni, nj});
            }
        }
        if (ans < 0) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
}
