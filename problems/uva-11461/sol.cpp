#include <cstdio>
int main() {
    int a, b;
    while (scanf("%d %d", &a, &b) == 2 && (a || b)) {
        int c = 0;
        for (int i = 1; i * i <= b; ++i) if (i * i >= a) ++c;
        printf("%d\n", c);
    }
}
