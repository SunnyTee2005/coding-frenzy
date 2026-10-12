#include <algorithm>
#include <cstdio>
#include <functional>
#include <vector>
using namespace std;
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        vector<long long> v;
        long long x;
        while (scanf("%lld", &x) == 1 && x) v.push_back(x);
        sort(v.begin(), v.end(), greater<long long>());
        const long long LIMIT = 5000000;
        long long total = 0;
        bool over = false;
        for (size_t i = 0; i < v.size() && !over; ++i) {
            long long p = 2;
            for (size_t e = 0; e <= i && !over; ++e) {
                p *= v[i];
                if (p > LIMIT) over = true;
            }
            total += p;
            if (total > LIMIT) over = true;
        }
        if (over) puts("Too expensive");
        else printf("%lld\n", total);
    }
}
