#include <algorithm>
#include <cstdio>
#include <string>
int main() {
    int t; scanf("%d", &t);
    for (int c = 1; c <= t; ++c) {
        long long n; scanf("%lld", &n);
        std::string s;
        if (n == 0) s = "0";
        while (n != 0) {
            long long r = n % -2;
            n /= -2;
            if (r < 0) { r += 2; n += 1; }
            s += char('0' + r);
        }
        std::reverse(s.begin(), s.end());
        printf("Case #%d: %s\n", c, s.c_str());
    }
}
