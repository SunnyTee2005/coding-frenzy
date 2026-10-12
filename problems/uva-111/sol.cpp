#include <algorithm>
#include <cstdio>
using namespace std;
int n, correct[25], student[25], dp[25][25];
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) { int r; scanf("%d", &r); correct[r] = i; }  // 第 r 名是第 i 件事
    for (;;) {
        bool ok = true;
        for (int i = 1; i <= n && ok; ++i) { int r; if (scanf("%d", &r) != 1) ok = false; else student[r] = i; }
        if (!ok) break;
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
                dp[i][j] = correct[i] == student[j] ? dp[i - 1][j - 1] + 1 : max(dp[i - 1][j], dp[i][j - 1]);
        printf("%d\n", dp[n][n]);
    }
}
