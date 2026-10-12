#include <cstdio>
#include <vector>
using namespace std;
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n, m, l; scanf("%d %d %d", &n, &m, &l);
        vector<vector<int>> g(n + 1);
        for (int i = 0; i < m; ++i) { int x, y; scanf("%d %d", &x, &y); g[x].push_back(y); }
        vector<bool> down(n + 1, false);
        int cnt = 0;
        while (l--) {
            int z; scanf("%d", &z);
            vector<int> st = {z};
            while (!st.empty()) {
                int u = st.back(); st.pop_back();
                if (down[u]) continue;
                down[u] = true; ++cnt;
                for (int v : g[u]) st.push_back(v);
            }
        }
        printf("%d\n", cnt);
    }
}
