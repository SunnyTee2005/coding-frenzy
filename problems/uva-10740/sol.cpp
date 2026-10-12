#include <cstdio>
#include <functional>
#include <queue>
#include <utility>
#include <vector>
using namespace std;
int main() {
    int n, m;
    while (scanf("%d %d", &n, &m) == 2 && (n || m)) {
        int x, y, k; scanf("%d %d %d", &x, &y, &k);
        vector<vector<pair<int, int>>> g(105);
        for (int i = 0; i < m; ++i) { int u, v, l; scanf("%d %d %d", &u, &v, &l); g[u].push_back({v, l}); }
        vector<int> cnt(105, 0);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        pq.push({0, x});
        long long ans = -1;
        while (!pq.empty()) {
            long long d = pq.top().first; int u = pq.top().second; pq.pop();
            if (++cnt[u] > k) continue;
            if (u == y && cnt[u] == k) { ans = d; break; }
            for (auto& e : g[u]) pq.push({d + e.second, e.first});
        }
        printf("%lld\n", ans);
    }
}
