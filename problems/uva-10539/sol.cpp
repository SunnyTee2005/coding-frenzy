#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
int main() {
    const long long LIM = 1000000000000LL;
    const int R = 1000000;
    vector<bool> comp(R + 1, false);
    vector<long long> almost;
    for (long long p = 2; p <= R; ++p) {
        if (comp[p]) continue;
        for (long long q = p * p; q <= R; q += p) comp[q] = true;
        for (long long x = p * p; x < LIM; x *= p) almost.push_back(x);
    }
    sort(almost.begin(), almost.end());
    int n; scanf("%d", &n);
    while (n--) {
        long long lo, hi; scanf("%lld %lld", &lo, &hi);
        printf("%d\n", (int)(upper_bound(almost.begin(), almost.end(), hi) - lower_bound(almost.begin(), almost.end(), lo)));
    }
}
