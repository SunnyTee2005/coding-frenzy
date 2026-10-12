#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
int main() {
    vector<pair<int, int>> t;  // (力量, 重量)
    int w, s;
    while (scanf("%d %d", &w, &s) == 2) t.push_back({s, w});
    sort(t.begin(), t.end());
    // dp[c]：疊 c 隻時的最小總重；力量小的放上面，依力量排序後逐隻考慮放在最底下
    const long long INF = 1LL << 60;
    vector<long long> dp(t.size() + 1, INF);
    dp[0] = 0;
    for (auto& x : t)
        for (int c = (int)t.size(); c >= 1; --c)
            if (dp[c - 1] + x.second <= x.first) dp[c] = min(dp[c], dp[c - 1] + x.second);
    int best = 0;
    for (int c = 0; c <= (int)t.size(); ++c) if (dp[c] < INF) best = c;
    printf("%d\n", best);
}
