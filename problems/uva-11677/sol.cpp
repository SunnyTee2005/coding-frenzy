#include <cstdio>
int main() {
    int h1, m1, h2, m2;
    while (scanf("%d %d %d %d", &h1, &m1, &h2, &m2) == 4 && (h1 || m1 || h2 || m2)) {
        int d = (h2 * 60 + m2) - (h1 * 60 + m1);
        if (d < 0) d += 1440;
        printf("%d\n", d);
    }
}
