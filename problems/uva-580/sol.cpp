#include <cstdio>
int main() {
    // safe[n]：長度 n、沒有連續 3 個 U 的排法數
    long long safe[35] = {1, 2, 4};
    for (int i = 3; i <= 30; ++i) safe[i] = safe[i - 1] + safe[i - 2] + safe[i - 3];
    int n;
    while (scanf("%d", &n) == 1 && n) printf("%lld\n", (1LL << n) - safe[n]);
}
