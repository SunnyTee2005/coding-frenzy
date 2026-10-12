#include <cstdio>
#include <vector>
using namespace std;
int nxt[50005], reach[50005], vis[50005];
int main() {
    int t; scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        int n; scanf("%d", &n);
        for (int i = 0; i < n; ++i) { int u, v; scanf("%d %d", &u, &v); nxt[u] = v; }
        for (int i = 1; i <= n; ++i) reach[i] = 0, vis[i] = 0;
        for (int s = 1; s <= n; ++s) {
            if (reach[s]) continue;
            // 沿著走到已知或本輪走過的點
            vector<int> path;
            int u = s;
            while (!reach[u] && !vis[u]) { vis[u] = s; path.push_back(u); u = nxt[u]; }
            if (!reach[u] && vis[u] == s) {
                // 找到新的環
                int len = 0, idx = (int)path.size() - 1;
                while (path[idx] != u) --idx;
                len = (int)path.size() - idx;
                for (int i = idx; i < (int)path.size(); ++i) reach[path[i]] = len;
                path.resize(idx);
            }
            for (int i = (int)path.size() - 1; i >= 0; --i) reach[path[i]] = reach[nxt[path[i]]] + 1;
        }
        int best = 1;
        for (int i = 2; i <= n; ++i) if (reach[i] > reach[best]) best = i;
        printf("Case %d: %d\n", cs, best);
    }
}
