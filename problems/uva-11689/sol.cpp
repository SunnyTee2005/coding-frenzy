#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        int e, f, c; scanf("%d %d %d", &e, &f, &c);
        int empty = e + f, drunk = 0;
        while (empty >= c) { int got = empty / c; drunk += got; empty = empty % c + got; }
        printf("%d\n", drunk);
    }
}
