#include <algorithm>
#include <cstdio>
#include <cstdlib>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int r, s[505]; scanf("%d", &r);
        for (int i = 0; i < r; ++i) scanf("%d", &s[i]);
        std::sort(s, s + r);
        long long sum = 0;
        for (int i = 0; i < r; ++i) sum += std::abs(s[i] - s[r / 2]);
        printf("%lld\n", sum);
    }
}
