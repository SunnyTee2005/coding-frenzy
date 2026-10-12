#include <cstdio>
#include <string>
int main() {
    long long n;
    while (scanf("%lld", &n) == 1 && n) {
        std::string b;
        int p = 0;
        for (long long x = n; x; x >>= 1) { b = char('0' + (x & 1)) + b; p += x & 1; }
        printf("The parity of %s is %d (mod 2).\n", b.c_str(), p);
    }
}
