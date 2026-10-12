#include <cstdio>
void bangla(long long n) {
    if (n >= 10000000) { bangla(n / 10000000); printf(" kuti"); n %= 10000000; }
    if (n >= 100000) { bangla(n / 100000); printf(" lakh"); n %= 100000; }
    if (n >= 1000) { bangla(n / 1000); printf(" hajar"); n %= 1000; }
    if (n >= 100) { bangla(n / 100); printf(" shata"); n %= 100; }
    if (n) printf(" %lld", n);
}
int main() {
    long long n;
    int cs = 0;
    while (scanf("%lld", &n) == 1) {
        printf("%4d.", ++cs);
        bangla(n);
        printf("\n");
    }
}
