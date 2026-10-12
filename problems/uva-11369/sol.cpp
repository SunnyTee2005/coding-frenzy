#include <algorithm>
#include <cstdio>
#include <functional>
#include <vector>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int n; scanf("%d", &n);
        std::vector<int> p(n);
        for (int &x : p) scanf("%d", &x);
        std::sort(p.begin(), p.end(), std::greater<int>());
        long long s = 0;
        for (int i = 2; i < n; i += 3) s += p[i];
        printf("%lld\n", s);
    }
}
