#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    while (n--) {
        long long x; scanf("%lld", &x);
        puts(x % 3 == 1 ? "NO" : "YES");
    }
}
