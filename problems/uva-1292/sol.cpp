#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
vector<int> ch[1505];
int dp[1505][2];  // dp[u][1]：u 放士兵時子樹最少人數
void dfs(int u) {
    dp[u][0] = 0; dp[u][1] = 1;
    for (int v : ch[u]) {
        dfs(v);
        dp[u][0] += dp[v][1];
        dp[u][1] += min(dp[v][0], dp[v][1]);
    }
}
int main() {
    int n;
    while (scanf("%d", &n) == 1) {
        vector<bool> isChild(n, false);
        for (int i = 0; i < n; ++i) ch[i].clear();
        for (int i = 0; i < n; ++i) {
            int u, k; scanf("%d:(%d)", &u, &k);
            for (int j = 0; j < k; ++j) { int v; scanf("%d", &v); ch[u].push_back(v); isChild[v] = true; }
        }
        int root = 0;
        while (isChild[root]) ++root;
        dfs(root);
        printf("%d\n", min(dp[root][0], dp[root][1]));
    }
}
