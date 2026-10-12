#include <cstdio>

typedef unsigned long long u64;

static u64 rev(u64 x) {
    u64 r = 0;
    while (x) { r = r * 10 + x % 10; x /= 10; }
    return r;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    while (n--) {
        u64 p;
        scanf("%llu", &p);
        int steps = 0;
        do {
            p += rev(p);
            ++steps;
        } while (p != rev(p));
        printf("%d %llu\n", steps, p);
    }
    return 0;
}
