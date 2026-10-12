#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
int memo[151][201][51];  // 用 10+1+1+1 會找回 5 元，5 元硬幣最多 100+50 枚
int total;  // 一開始的總金額
int go(int c, int n5, int n10, int bought) {
    if (c == 0) return 0;
    int& r = memo[c][n5][n10];
    if (r >= 0) return r;
    int n1 = total - 8 * bought - 5 * n5 - 10 * n10;
    r = 1 << 29;
    if (n10 >= 1) r = min(r, 1 + go(c - 1, n5, n10 - 1, bought + 1));                       // 10 → 找 2 個 1
    if (n5 >= 2) r = min(r, 2 + go(c - 1, n5 - 2, n10, bought + 1));                        // 5+5 → 找 2 個 1
    if (n10 >= 1 && n1 >= 3) r = min(r, 4 + go(c - 1, n5 + 1, n10 - 1, bought + 1));        // 10+1+1+1 → 找 5
    if (n5 >= 1 && n1 >= 3) r = min(r, 4 + go(c - 1, n5 - 1, n10, bought + 1));             // 5+1+1+1
    if (n1 >= 8) r = min(r, 8 + go(c - 1, n5, n10, bought + 1));                            // 8 個 1
    return r;
}
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int c, n1, n5, n10; scanf("%d %d %d %d", &c, &n1, &n5, &n10);
        total = n1 + 5 * n5 + 10 * n10;
        memset(memo, -1, sizeof memo);
        printf("%d\n", go(c, n5, n10, 0));
    }
}
