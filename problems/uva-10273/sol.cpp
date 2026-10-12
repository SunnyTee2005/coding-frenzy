#include <cstdio>
#include <vector>
using namespace std;
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n; scanf("%d", &n);
        vector<vector<int>> milk(n);
        for (auto& c : milk) { int ti; scanf("%d", &ti); c.resize(ti); for (int& x : c) scanf("%d", &x); }
        vector<bool> alive(n, true);
        int left = n, lastDay = 0, quiet = 0;
        // 週期最多 lcm(1..10) = 2520 天；連續 2520 天沒有牛被吃就不會再有
        for (int day = 1; left > 0 && quiet < 2520; ++day) {
            int best = 1 << 30, who = -1, ties = 0;
            for (int i = 0; i < n; ++i) {
                if (!alive[i]) continue;
                int v = milk[i][(day - 1) % milk[i].size()];
                if (v < best) { best = v; who = i; ties = 1; }
                else if (v == best) ++ties;
            }
            if (ties == 1) { alive[who] = false; --left; lastDay = day; quiet = 0; }
            else ++quiet;
        }
        printf("%d %d\n", left, lastDay);
    }
}
