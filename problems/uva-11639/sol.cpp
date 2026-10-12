#include <algorithm>
#include <cstdio>
using namespace std;
int main() {
    int n; scanf("%d", &n);
    for (int c = 1; c <= n; ++c) {
        int a1, b1, a2, b2, c1, d1, c2, d2;
        scanf("%d %d %d %d %d %d %d %d", &a1, &b1, &a2, &b2, &c1, &d1, &c2, &d2);
        int w = max(0, min(a2, c2) - max(a1, c1)), h = max(0, min(b2, d2) - max(b1, d1));
        int strong = w * h;
        int weak = (a2 - a1) * (b2 - b1) + (c2 - c1) * (d2 - d1) - 2 * strong;
        printf("Night %d: %d %d %d\n", c, strong, weak, 10000 - strong - weak);
    }
}
