#include <cstdio>
int main() {
    long long a, b;
    while (scanf("%lld %lld", &a, &b) == 2) {
        printf("[%lld", a / b);
        long long r = a % b;
        a = b; b = r;
        char sep = ';';
        while (b) {
            printf("%c%lld", sep, a / b);
            sep = ',';
            r = a % b; a = b; b = r;
        }
        printf("]\n");
    }
}
