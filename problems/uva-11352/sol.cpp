#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int m, n; cin >> m >> n;
        vector<string> g(m);
        for (auto &r : g) cin >> r;
        vector<vector<bool>> bad(m, vector<bool>(n, false));
        int kx[] = {1, 1, -1, -1, 2, 2, -2, -2}, ky[] = {2, -2, 2, -2, 1, -1, 1, -1};
        int sx = 0, sy = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j) {
                if (g[i][j] == 'A') { sx = i; sy = j; }
                if (g[i][j] != 'Z') continue;
                bad[i][j] = true;
                for (int d = 0; d < 8; ++d) {
                    int x = i + kx[d], y = j + ky[d];
                    if (x >= 0 && x < m && y >= 0 && y < n && g[x][y] != 'A' && g[x][y] != 'B') bad[x][y] = true;
                }
            }
        vector<vector<int>> dist(m, vector<int>(n, -1));
        queue<pair<int, int>> q;
        dist[sx][sy] = 0; q.push({sx, sy});
        int ans = -1;
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            if (g[x][y] == 'B') { ans = dist[x][y]; break; }
            for (int dx = -1; dx <= 1; ++dx)
                for (int dy = -1; dy <= 1; ++dy) {
                    int a = x + dx, b = y + dy;
                    if ((dx || dy) && a >= 0 && a < m && b >= 0 && b < n && !bad[a][b] && dist[a][b] < 0) {
                        dist[a][b] = dist[x][y] + 1; q.push({a, b});
                    }
                }
        }
        if (ans < 0) cout << "King Peter, you can't go now!\n";
        else cout << "Minimal possible length of a trip is " << ans << "\n";
    }
}
