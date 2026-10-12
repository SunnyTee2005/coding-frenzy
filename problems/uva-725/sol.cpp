#include <cstdio>
bool distinct(int a, int b) {
    int used = 0;
    for (int i = 0; i < 5; ++i) { used |= 1 << (a % 10); a /= 10; }
    for (int i = 0; i < 5; ++i) { used |= 1 << (b % 10); b /= 10; }
    return used == (1 << 10) - 1;
}
int main() {
    int n;
    bool first = true;
    while (scanf("%d", &n) == 1 && n) {
        if (!first) printf("\n");
        first = false;
        bool any = false;
        for (int den = 1234; den * n <= 98765; ++den)
            if (distinct(den * n, den)) { printf("%05d / %05d = %d\n", den * n, den, n); any = true; }
        if (!any) printf("There are no solutions for %d.\n", n);
    }
}
