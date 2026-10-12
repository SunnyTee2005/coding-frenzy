#include <algorithm>
#include <cstdio>
using namespace std;
int a[30005];
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n; scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
        // odd：長度為奇數（下一步要往下）的最長子序列；even：長度為偶數（下一步要往上）
        int odd = 1, even = 0;
        for (int i = 1; i < n; ++i) {
            if (a[i] < a[i - 1]) even = max(even, odd + 1);
            else if (a[i] > a[i - 1] && even > 0) odd = max(odd, even + 1);
        }
        printf("%d\n", max(odd, even));
    }
}
