#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
int m;
bool cmp(int a, int b) {
    int ra = a % m, rb = b % m;
    if (ra != rb) return ra < rb;
    bool oa = a % 2 != 0, ob = b % 2 != 0;
    if (oa != ob) return oa;
    return oa ? a > b : a < b;
}
int main() {
    int n;
    while (scanf("%d %d", &n, &m) == 2) {
        printf("%d %d\n", n, m);
        if (n == 0 && m == 0) break;
        vector<int> v(n);
        for (int& x : v) scanf("%d", &x);
        sort(v.begin(), v.end(), cmp);
        for (int x : v) printf("%d\n", x);
    }
}
