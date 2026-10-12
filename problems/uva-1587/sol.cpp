#include <algorithm>
#include <cstdio>
#include <utility>
using namespace std;
int main() {
    pair<int, int> p[6];
    while (scanf("%d %d", &p[0].first, &p[0].second) == 2) {
        for (int i = 1; i < 6; ++i) scanf("%d %d", &p[i].first, &p[i].second);
        for (auto& q : p) if (q.first > q.second) swap(q.first, q.second);
        sort(p, p + 6);
        bool ok = p[0] == p[1] && p[2] == p[3] && p[4] == p[5]
               && p[0].first == p[2].first && p[0].second == p[4].first && p[2].second == p[4].second;
        puts(ok ? "POSSIBLE" : "IMPOSSIBLE");
    }
}
