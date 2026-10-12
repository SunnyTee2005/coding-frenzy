#include <algorithm>
#include <array>
#include <cstdio>
#include <numeric>
#include <vector>
using namespace std;
int parent[10005];
int find(int x) { return parent[x] == x ? x : parent[x] = find(parent[x]); }
int main() {
    int c; scanf("%d", &c);
    while (c--) {
        int n, m; scanf("%d %d", &n, &m);
        vector<array<int, 3>> e(m);
        long long total = 0;
        for (auto& x : e) { scanf("%d %d %d", &x[1], &x[2], &x[0]); total += x[0]; }
        sort(e.rbegin(), e.rend());  // 最大生成樹：留下的路不放攝影機
        iota(parent, parent + n + 1, 0);
        long long kept = 0;
        for (auto& x : e) {
            int a = find(x[1]), b = find(x[2]);
            if (a != b) { parent[a] = b; kept += x[0]; }
        }
        printf("%lld\n", total - kept);
    }
}
