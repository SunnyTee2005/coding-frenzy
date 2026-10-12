#include <cstdio>
#include <string>
#include <vector>

int main() {
    std::vector<long long> fib = {1, 2};
    while (fib.back() < 100000000LL) fib.push_back(fib[fib.size() - 1] + fib[fib.size() - 2]);
    int n;
    if (scanf("%d", &n) != 1) return 0;
    while (n--) {
        long long x;
        scanf("%lld", &x);
        long long left = x;
        std::string rep;
        bool started = false;
        for (int i = (int)fib.size() - 1; i >= 0; --i) {
            if (fib[i] <= left) {
                left -= fib[i];
                rep += '1';
                started = true;
            } else if (started) {
                rep += '0';
            }
        }
        printf("%lld = %s (fib)\n", x, rep.c_str());
    }
    return 0;
}
