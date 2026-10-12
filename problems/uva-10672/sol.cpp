#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;
vector<int> ch[10005];
int marbles[10005];
long long moves;
long long dfs(int u) {
    // 回傳子樹多出（正）或缺少（負）的彈珠數，每顆要經過連到父親的那條邊
    long long extra = marbles[u] - 1;
    for (int v : ch[u]) extra += dfs(v);
    moves += llabs(extra);
    return extra;
}
int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        vector<bool> isChild(n + 1, false);
        for (int i = 1; i <= n; ++i) ch[i].clear();
        for (int i = 0; i < n; ++i) {
            int v, m, d; scanf("%d %d %d", &v, &m, &d);
            marbles[v] = m;
            while (d--) { int c; scanf("%d", &c); ch[v].push_back(c); isChild[c] = true; }
        }
        int root = 1;
        while (isChild[root]) ++root;
        moves = 0;
        long long top = dfs(root);
        moves -= llabs(top);  // 根上面沒有邊
        printf("%lld\n", moves);
    }
}
