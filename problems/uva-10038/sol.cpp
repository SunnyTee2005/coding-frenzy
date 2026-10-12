#include <cstdio>
#include <cstdlib>
#include <cstring>
bool seen[3005];
int main() {
    int n;
    while (scanf("%d", &n) == 1) {
        long long prev, x;
        scanf("%lld", &prev);
        memset(seen, 0, sizeof seen);
        bool ok = true;
        for (int i = 1; i < n; ++i) {
            scanf("%lld", &x);
            long long d = llabs(x - prev);
            if (d < 1 || d > n - 1 || seen[d]) ok = false;
            else seen[d] = true;
            prev = x;
        }
        puts(ok ? "Jolly" : "Not jolly");
    }
}
