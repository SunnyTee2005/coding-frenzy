#include <cstdio>
int main() {
    int n;
    while (scanf("%d", &n) == 1 && n) {
        int x = n, cnt = 0;
        for (int p = 2; (long long)p * p <= x; ++p)
            if (x % p == 0) { ++cnt; while (x % p == 0) x /= p; }
        if (x > 1) ++cnt;
        printf("%d : %d\n", n, cnt);
    }
}
