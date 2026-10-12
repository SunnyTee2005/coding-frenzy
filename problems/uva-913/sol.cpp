#include <cstdio>
int main() {
    long long n;
    while (scanf("%lld", &n) == 1) {
        long long m = (n + 1) / 2;
        long long last = 2 * m * m - 1;
        printf("%lld\n", 3 * last - 6);
    }
}
