#include <cstdio>
int main() {
    int d; scanf("%d", &d);
    while (d--) {
        long long n, m; scanf("%lld %lld", &n, &m);
        // S(n, m) 的奇偶 = C(n - ceil((m+1)/2), (m-1)/2) 的奇偶；C(a, b) 為奇數 ⇔ (a & b) == b
        long long z = n - (m + 2) / 2, w = (m - 1) / 2;
        int ans = (m == 0) ? (n == 0) : (z >= 0 && w >= 0 && (z & w) == w ? 1 : 0);
        printf("%d\n", ans);
    }
}
