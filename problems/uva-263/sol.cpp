#include <algorithm>
#include <cstdio>
#include <functional>
#include <set>
#include <string>
using namespace std;
int main() {
    long long n;
    while (scanf("%lld", &n) == 1 && n) {
        printf("Original number was %lld\n", n);
        set<long long> seen = {n};
        for (;;) {
            string s = to_string(n);
            sort(s.begin(), s.end(), greater<char>());
            long long hi = stoll(s);
            sort(s.begin(), s.end());
            long long lo = stoll(s);
            n = hi - lo;
            printf("%lld - %lld = %lld\n", hi, lo, n);
            if (!seen.insert(n).second) break;
        }
        printf("Chain length %d\n\n", (int)seen.size());
    }
}
