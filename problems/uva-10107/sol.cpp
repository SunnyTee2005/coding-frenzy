#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
int main() {
    vector<long long> v;
    long long x;
    while (scanf("%lld", &x) == 1) {
        v.insert(upper_bound(v.begin(), v.end(), x), x);
        size_t n = v.size();
        printf("%lld\n", n % 2 ? v[n / 2] : (v[n / 2 - 1] + v[n / 2]) / 2);
    }
}
