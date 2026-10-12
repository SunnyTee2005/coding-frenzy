#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    for (int c = 0; c < t; ++c) {
        int a, f; scanf("%d %d", &a, &f);
        if (c) printf("\n");
        for (int w = 0; w < f; ++w) {
            if (w) printf("\n");
            for (int h = 1; h <= a; ++h) { for (int i = 0; i < h; ++i) putchar('0' + h); putchar('\n'); }
            for (int h = a - 1; h >= 1; --h) { for (int i = 0; i < h; ++i) putchar('0' + h); putchar('\n'); }
        }
    }
}
