#include <cstdio>
int main() {
    int n;
    puts("PERFECTION OUTPUT");
    while (scanf("%d", &n) == 1 && n) {
        int s = 0;
        for (int d = 1; d < n; ++d) if (n % d == 0) s += d;
        printf("%5d  %s\n", n, s == n ? "PERFECT" : s < n ? "DEFICIENT" : "ABUNDANT");
    }
    puts("END OF OUTPUT");
}
