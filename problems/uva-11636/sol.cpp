#include <cstdio>
int main() {
    int n, cs = 0;
    while (scanf("%d", &n) == 1 && n > 0) {
        int p = 0;
        for (int lines = 1; lines < n; lines *= 2) ++p;
        printf("Case %d: %d\n", ++cs, p);
    }
}
