#include <cstdio>
#include <vector>
using namespace std;
vector<vector<long long>> all;
vector<long long> cur;
void go(long long n, long long from) {
    for (long long f = from; f * f <= n; ++f)
        if (n % f == 0) {
            cur.push_back(f);
            go(n / f, f);
            cur.pop_back();
        }
    if (!cur.empty() && n >= from) {  // 剩下的 n 當作最後一個因數
        cur.push_back(n);
        all.push_back(cur);
        cur.pop_back();
    }
}
int main() {
    long long n;
    while (scanf("%lld", &n) == 1 && n) {
        all.clear();
        go(n, 2);
        printf("%d\n", (int)all.size());
        for (auto& v : all) {
            for (size_t i = 0; i < v.size(); ++i) printf(i ? " %lld" : "%lld", v[i]);
            printf("\n");
        }
    }
}
