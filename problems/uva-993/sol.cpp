#include <algorithm>
#include <cstdio>
#include <string>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        long long n; scanf("%lld", &n);
        if (n < 10) { printf("%lld\n", n == 0 ? 10 : n); continue; }
        std::string d;
        for (int f = 9; f >= 2; --f)
            while (n % f == 0) { d += char('0' + f); n /= f; }
        if (n != 1) { puts("-1"); continue; }
        std::sort(d.begin(), d.end());
        puts(d.c_str());
    }
}
