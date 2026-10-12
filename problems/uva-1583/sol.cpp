#include <cstdio>
int gen[100105];
int main() {
    for (int n = 100000; n >= 1; --n) {
        int m = n;
        for (int x = n; x; x /= 10) m += x % 10;
        if (m <= 100000) gen[m] = n;  // 由大到小填，最後留下最小的
    }
    int t; scanf("%d", &t);
    while (t--) { int n; scanf("%d", &n); printf("%d\n", gen[n]); }
}
