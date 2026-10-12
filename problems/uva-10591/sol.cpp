#include <cstdio>
#include <set>
int next(int n) { int s = 0; for (; n; n /= 10) s += (n % 10) * (n % 10); return s; }
int main() {
    int t; scanf("%d", &t);
    for (int c = 1; c <= t; ++c) {
        int n; scanf("%d", &n);
        std::set<int> seen;
        int x = n;
        while (x != 1 && !seen.count(x)) { seen.insert(x); x = next(x); }
        printf("Case #%d: %d is %s number.\n", c, n, x == 1 ? "a Happy" : "an Unhappy");
    }
}
