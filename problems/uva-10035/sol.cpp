#include <cstdio>

int main() {
    unsigned long long a, b;
    while (scanf("%llu %llu", &a, &b) == 2 && (a || b)) {
        int carry = 0, count = 0;
        while (a || b) {
            int s = (int)(a % 10 + b % 10) + carry;
            carry = s >= 10;
            count += carry;
            a /= 10;
            b /= 10;
        }
        if (count == 0) puts("No carry operation.");
        else if (count == 1) puts("1 carry operation.");
        else printf("%d carry operations.\n", count);
    }
    return 0;
}
