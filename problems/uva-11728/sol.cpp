#include <cstdio>
int main() {
    int best[1001];
    for (int s = 0; s <= 1000; ++s) best[s] = -1;
    for (int x = 1; x <= 1000; ++x) {
        int sum = 0;
        for (int d = 1; d <= x; ++d) if (x % d == 0) sum += d;
        if (sum <= 1000) best[sum] = x;
    }
    int s, c = 0;
    while (scanf("%d", &s) == 1 && s) printf("Case %d: %d\n", ++c, best[s]);
}
